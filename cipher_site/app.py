from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elements = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
        "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs",
        "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]
    greek = ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω"]
    hiragana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
    eto = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    italian = "A B C D E F G H I L M N O P Q R S T U V Z".split()
    russian = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".split()
    spanish = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z".split()

    rows = []
    for i in range(118):
        row = {
            'number': i + 1,
            'digit': i + 1,
            'alphabet': alphabets[i] if i < len(alphabets) else '',
            'element': elements[i] if i < len(elements) else '',
            'greek': greek[i] if i < len(greek) else '',
            'hiragana': hiragana[i] if i < len(hiragana) else '',
            'eto': eto[i] if i < len(eto) else '',
            'italian': italian[i] if i < len(italian) else '',
            'russian': russian[i] if i < len(russian) else '',
            'spanish': spanish[i] if i < len(spanish) else ''
        }
        rows.append(row)

    return render_template('index.html', rows=rows)
