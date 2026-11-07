# element checker
from pyscript import display, document

elements = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'B': 'Boron',
    'C': 'Carbon',
    'N': 'Nitrogen',
    'O': 'Oxygen',
    'F': 'Fluorine',
    'Ne': 'Neon',
    'Si': 'Silicon',
    'P': 'Phosphorus',
    'S': 'Sulfur',
    'Cl': 'Chlorine',
    'Ar': 'Argon',
    'Ge': 'Germanium',
    'As': 'Arsenic',
    'Se': 'Selenium',
    'Br': 'Bromine',
    'Kr': 'Krypton',
    'Sb': 'Antimony',
    'Te': 'Tellurium',
    'I': 'Iodine',
    'Xe': 'Xenon',
    'At': 'Astatine',
    'Rn': 'Radon',
    'Ts': 'Tennesine',
    'Og': 'Oganesson',
}
atomic_number = {
    'H': '1',
    'He': '2',
    'B': '5',
    'C': '6',
    'N': '7',
    'O': '8',
    'F': '9',
    'Ne': '10',
    'Si': '14',
    'P': '15',
    'S': '16',
    'Cl': '17',
    'Ar': '18',
    'Ge': '32',
    'As': '33',
    'Se': '34',
    'Br': '35',
    'Kr': '36',
    'Sb': '51',
    'Te': '52',
    'I': '53',
    'Xe': '54',
    'At': '85',
    'Rn': '86',
    'Ts': '117',
    'Og': '118',    
}
atomic_mass = {
    'H': '1',
    'He': '4',
    'B': '10.81',
    'C': '12.01',
    'N': '14',
    'O': '16',
    'F': '19',
    'Ne': '20.18',
    'Si': '28.09',
    'P': '30.97',
    'S': '32.07',
    'Cl': '35.45',
    'Ar': '39.95',
    'Ge': '72.64',
    'As': '74.92',
    'Se': '78.96',
    'Br': '79.90',
    'Kr': '83.8',
    'Sb': '121.76',
    'Te': '127.6',
    'I': '126.90',
    'Xe': '131.29',
    'At': '210',
    'Rn': '222',
    'Ts': '260.9',
    'Og': '294',    
}
def check_element(e):
    document.getElementById('output').innerHTML = " "
    text = document.getElementById('element').value.strip().title()
    symbol = text
    element_name = elements.get(text)
    number = atomic_number.get(text)
    mass = atomic_mass.get(text)

    display_element = (
        (f'This element is not found: {symbol}',), 
        (
            f'Symbol: {symbol}', 
            f'Element Name: {element_name}',
            f'Atomic Number: {number}',
            f'Atomic Mass: {mass}'
        )
    )

    display(*display_element[text in elements], target='output')
