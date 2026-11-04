# element checker
from pyscript import display, document

elements = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne',
    'Silicon': 'Si',
    'Phosphorus': 'P',
    'Sulfur': 'S',
    'Chlorine': 'Cl',
    'Argon': 'Ar',
    'Germanium': 'Ge',
    'Arsenic': 'As',
    'Selenium': 'Se',
    'Bromine': 'Br',
    'Krypton': 'Kr',
    'Antimony': 'Sb',
    'Tellurium': 'Te',
    'Iodine': 'I',
    'Xenon': 'Xe',
    'Astatine': 'At',
    'Radon': 'Rn',
    'Tennessine': 'Ts',
    'Oganesson': 'Og',
}
atomic_number = {
    'Hydrogen': '1',
    'Helium': '2',
    'Boron': '5',
    'Carbon': '6',
    'Nitrogen': '7',
    'Oxygen': '8',
    'Fluorine': '9',
    'Neon': '10',
    'Silicon': '14',
    'Phosphorus': '15',
    'Sulfur': '16',
    'Chlorine': '17',
    'Argon': '18',
    'Germanium': '32',
    'Arsenic': '33',
    'Selenium': '34',
    'Bromine': '35',
    'Krypton': '36',
    'Antimony': '51',
    'Tellurium': '52',
    'Iodine': '53',
    'Xenon': '54',
    'Astatine': '85',
    'Radon': '86',
    'Tennessine': '117',
    'Oganesson': '118',    
}
atomic_mass = {
    'Hydrogen': '1',
    'Helium': '4',
    'Boron': '10.81',
    'Carbon': '12.01',
    'Nitrogen': '14',
    'Oxygen': '16',
    'Fluorine': '19',
    'Neon': '20.18',
    'Silicon': '28.09',
    'Phosphorus': '30.97',
    'Sulfur': '32.07',
    'Chlorine': '35.45',
    'Argon': '39.95',
    'Germanium': '72.64',
    'Arsenic': '74.92',
    'Selenium': '78.96',
    'Bromine': '79.90',
    'Krypton': '83.8',
    'Antimony': '121.76',
    'Tellurium': '127.6',
    'Iodine': '126.90',
    'Xenon': '131.29',
    'Astatine': '210',
    'Radon': '222',
    'Tennessine': '260.9',
    'Oganesson': '294',    
}
text = document.getElementById('element').value
def check_element(e):
    # Retrieve current input value when triggered and standardise casing
    text = document.getElementById('element').value.strip().title()
    
    # Clear previous output
    document.getElementById('output').innerHTML = ""

    if text in elements:
        display(f'Symbol: {elements.get(text)}', target='output')
        display(f'Element: {text}', target='output')
        display(f'Atomic Number: {atomic_number.get(text)}', target='output')
        display(f'Atomic Mass: {atomic_mass.get(text)}', target='output')
    else:
        display('Element not found.', target='output')