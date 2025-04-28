# extractor.py

# Some common garbage headings we want to ignore
GARBAGE_HEADINGS = [
    "Learn More", "Contact Us", "Sign In", "Let's make it happen!",
    "Privacy Policy", "Terms of Service", "Start Free Trial", "Log In"
]

def is_valid_heading(text):
    if not text:
        return False
    if len(text) < 3:
        return False
    if text in GARBAGE_HEADINGS:
        return False
    return True

def extract_modules_and_submodules(soup):
    modules = {}
    current_module = None
    current_submodule = None

    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        text = tag.get_text(strip=True)
        if not is_valid_heading(text):
            continue

        if tag.name == 'h1':
            current_module = text
            modules[current_module] = {"Description": "", "Submodules": {}}
            current_submodule = None  # Reset submodule

        elif tag.name == 'h2' and current_module:
            current_submodule = text
            modules[current_module]["Submodules"][current_submodule] = ""

        elif tag.name == 'p':
            if current_module and current_submodule:
                if modules[current_module]["Submodules"].get(current_submodule) == "":
                    modules[current_module]["Submodules"][current_submodule] = text
            elif current_module:
                if modules[current_module]["Description"] == "":
                    modules[current_module]["Description"] = text

    return modules