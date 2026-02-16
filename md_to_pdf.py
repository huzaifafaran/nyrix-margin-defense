import markdown
from xhtml2pdf import pisa
import os
import pathlib

def convert_md_to_pdf(md_file_path, pdf_file_path):
    # Read Markdown content
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['tables'])

    # Custom Page Breaks
    html_content = html_content.replace('<!-- pagebreak -->', '<pdf:nextpage />')
    
    # Wrap tables to prevent breaking inside, and ensure headings stay with them
    # This is a bit of a hack for xhtml2pdf, but <pdf:nextpage /> before table if needed is hard to calculate.
    # We rely on CSS 'page-break-inside: avoid' which xhtml2pdf supports on <div> or <table>
    html_content = html_content.replace('<table>', '<table style="-pdf-keep-with-next: true; page-break-inside: avoid;">')
    
    # Add page number to footer
    html_footer = """
    <div id="footer_content" style="font-size: 9px; text-align: center; border-top: 1px solid #eee; padding-top: 5px;">Page <pdf:pagenumber> of <pdf:pagecount></div>
    """
    # Add basic styling for PDF with Nyrix Branding
    # Branding Colors: Purple (#8A5CF5), Dark BG (#0A0A0A) - adapted for white paper
    # Use absolute path for image, xhtml2pdf prefers this over URIs for local files usually
    logo_path = r"c:\Users\Gigabyte\Desktop\lucky cement testing\logo icon no-bg.png"
    if not os.path.exists(logo_path):
        print(f"Warning: Logo not found at {logo_path}")
    
    styled_html = f"""
    <html>
    <head>
    <style>
        /* Removed simple @page for stability - xhtml2pdf has issues with complex page rules in some versions */
        @page {{
            margin: 2cm;
        }}
        body {{ 
            font-family: Helvetica, Arial, sans-serif; 
            font-size: 11px; 
            line-height: 1.6; 
            color: #333; 
            text-align: justify;
        }}
        
        /* Header Section with Logo */
        .header-container {{
            text-align: right;
            margin-bottom: 20px;
            /* border-bottom: 3px solid #8A5CF5; Removed per user request */
            padding-bottom: 15px;
        }}
        .logo {{
            width: 120px;
            height: auto;
        }}
        
        /* Typography Branding */
        h1 {{ 
            color: #8A5CF5; 
            font-size: 24px;
            margin-top: 0px; 
            margin-bottom: 10px;
            text-align: left; /* Keep headers left-aligned usually looks better even with justified body */
        }}
        h2 {{ 
            color: #2c3e50; 
            font-size: 16px;
            margin-top: 25px; 
            margin-bottom: 10px;
            /* border-bottom: 1px solid #e0e0e0; Removed per user request */
            padding-bottom: 5px; 
            text-align: left;
        }}
        h3 {{ 
            color: #8A5CF5; 
            font-size: 13px;
            margin-top: 15px; 
            margin-bottom: 5px;
            text-transform: uppercase;
            text-align: left;
        }}
        
        /* Remove Horizontal Rules */
        hr {{
            display: none;
            border: 0;
        }}
        
        /* Table Styling */
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        th, td {{ border: 1px solid #e0e0e0; padding: 10px; text-align: left; }}
        th {{ 
            background-color: #f8f5ff; /* Very light purple tint */
            color: #5c3eb5; /* Darker purple for text */
            font-weight: bold;
            border-bottom: 2px solid #8A5CF5;
        }}
        
        /* Blockquotes/Notes */
        blockquote {{ 
            background-color: #f8f9fa; 
            border-left: 4px solid #8A5CF5; 
            margin: 1.5em 0; 
            padding: 10px 15px; 
            font-style: italic; 
            color: #555;
        }}
        code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
        
        /* Pricing Table Specifics */
        tr:nth-child(even) {{ background-color: #fcfcfc; }}
        
    </style>
    </head>
    <body>
    <div class="header-container">
        <img src="{logo_path}" class="logo" />
    </div>
    {html_content}
    </body>
    </html>
    """

    # Write HTML to temporary file (optional, for debugging)
    with open('temp_debug.html', 'w', encoding='utf-8') as f:
        f.write(styled_html)
    print("Saved temp_debug.html for verification")

    # Convert HTML to PDF
    with open(pdf_file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(styled_html, dest=pdf_file)

    if pisa_status.err:
        print(f"Error converting Markdown to PDF: {pisa_status.err}")
        return False
    else:
        print(f"Successfully created PDF: {pdf_file_path}")
        return True

if __name__ == "__main__":
    md_path = r"C:\Users\Gigabyte\.gemini\antigravity\brain\7f56243b-8adf-4097-bd8b-c4bc9028ae36\Nyrix_AI_Proposal_Lucky_Cement.md"
    # Using a new filename to avoid file lock issues
    pdf_path = r"c:\Users\Gigabyte\Desktop\lucky cement testing\Nyrix_Proposal_Final.pdf"
    
    if os.path.exists(md_path):
        convert_md_to_pdf(md_path, pdf_path)
    else:
        print(f"Markdown file not found: {md_path}")
