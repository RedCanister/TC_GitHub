import pandas as pd
import streamlit as st
import pickle

#Título
st.write("""
Prevendo Intervalo de Estrelas no GitHub\n
App que utiliza Machine Learning para prever possível quantia de estrelas
""")

#Cabeçalho
st.subheader('Informações sobre os dados')

#Nome do Usuário
user_input = st.sidebar.text_input('Digite seu nome')

st.write(f'Usuário: {user_input}')

language1 = ['TypeScript', 'Python', 'JavaScript', 'Shell', 'Batchfile', 'MATLAB', 'Java', 'Groovy', 'Zig', 'HCL', 'Lua', 'Liquid', 'Rust', 'HTML', 'CSS', 'PHP', 
 'Solidity', 'Vue', 'R', 'Markdown', 'Ruby', 'Mustache', 'C++', 'Go', 'C#'
 'PowerShell', 'Svelte', 'CMake', 'Smarty', 'Jupyter Notebook', 'Nix', 'JSON', 
 'Starlark', 'C', 'Dart', 'Scala', 'Kotlin', 'SCSS', 'Haskell', 'SystemVerilog', 
 'Roff', 'Perl', 'Swift', 'Makefile', 'Dockerfile', 'Blade',  'TeX', 
 'Visual Basic .NET', 'reStructuredText', 'Fortran', 'Apex' 'Astro', 
 'Handlebars', 'TSV', 'Jinja', 'LLVM', 'Julia', 'Rich Text Format', 
 'Mathematica', 'Emacs Lisp', 'ShaderLab', 'Pascal', 'MDX' 'GDScript', 
 'Assembly', 'Nim', 'PLpgSQL', 'Elixir', 'Common Lisp', 'OCaml' 'TSQL', 
 'Verilog', 'Meson', 'SQL', 'Typst', 'D', 'kvlang', 'DIGITAL Command Language', 
 'DM', 'Bicep', 'Ink', 'Objective-C', 'SourcePawn', 'Cuda', 'SaltStack', 'Scheme', 
 'Smalltalk', 'VHDL', 'BitBake', 'F#', 'Processing', 'Cairo', 'Racket', 'GLSL', 
 'message', 'Hack', 'Portugol', 'XML', 'CodeQL']

language2 = ['JavaScript', 'HTML', 'CSS', 'Dockerfile', 'Shell', 'Batchfile', 'SCSS',
 'TypeScript', 'GAP', 'Vue', 'Groovy', 'JSON', 'Makefile', 'Solidity', 'Smarty',
 'Starlark', 'PowerShell', 'C', 'Python', 'Svelte', 'C++', 'Inno Setup', 'Swift',
 'YAML', 'Markdown', 'TeX', 'WebAssembly', 'Roff', 'CMake', 'Java', 'Lua',
 'PLpgSQL', 'Jupyter Notebook', 'Haskell', 'Dart', 'Nix', 'Go', 'GLSL', 'Hack',
 'Kotlin', 'Awk', 'Blade', 'PHP', 'EJS', 'Assembly', 'Scheme', 'Rebol', 'XSLT',
 'LLVM', 'MDX', 'Gherkin', 'Rust', 'TSQL', 'C#', 'ShaderLab', 'R', 'Cython', 'HCL',
 'Astro', 'Ruby', 'Twig', 'Nunjucks', 'Visual Basic', 'Scala', 'Jinja', 'Fortran',
 'PLSQL', 'jq', 'Vim Script', 'Mustache', 'Brainfuck', 'MATLAB', 'HLSL',
 'Handlebars', 'Elixir', 'VHDL', 'Cypher', 'Just', 'Tcl', 'Emacs Lisp',
 'Smalltalk', 'FreeMarker', 'YARA','Objective-C', 'Noir', 'PureBasic', 'Perl',
 'Antlers', 'Yacc', 'ANTLR', 'Objective-C++', 'QML', 'BASIC', 'Metal', 'Mako',
 'MAXScript', 'KerboScript', 'Pug', 'Thrift', 'Csound Score', 'Fluent',
 'StringTemplate', 'Meson', 'Verilog', 'Nim', 'Dune', 'Cuda', 'Zig', 'M4',
 'BitBake', 'CoffeeScript', 'Sass', 'Clojure', 'VCL', 'SWIG', 'Mathematica',
 'AGS Script', 'Less', 'Jsonnet', 'mIRC Script', 'documentation_url', 'Liquid',
 'Puppet', 'Bicep', 'ASP.NET', 'Rich Text Format']

language3 = ['Shell', 'HTML', 'JavaScript', 'CSS', 'SCSS', 'Sage', 'Dockerfile', 'C',
 'Just', 'YAML', 'CMake', 'Vyper', 'Ruby', 'Groovy', 'PHP', 'Python', 'Dart',
 'Procfile', 'Logos', 'MDX', 'Java', 'Makefile', 'Kotlin', 'PLpgSQL', 'Starlark',
 'Batchfile', 'JSON', 'Jinja', 'C#', 'TypeScript', 'Cairo', 'Go', 'ShaderLab',
 'Elm', 'FreeMarker', 'Cuda', 'Cadence', 'C++', 'HCL', 'Cython',
 'Rich Text Format', 'Sass', 'Jupyter Notebook', 'SWIG', 'M4', 'NCL', 'Perl',
 'PowerShell', 'Gnuplot', 'Blade', 'Roff', 'HLSL', 'Vue', 'Fortran', 'Bicep',
 'Handlebars', 'TeX', 'Smarty', 'Mathematica', 'Twig', 'R', 'Assembly',
 'Objective-C', 'TSQL', 'XSLT', 'Solidity', 'Jsonnet', 'LLVM', 'Nix', 'Rust',
 'Forth', 'Less', 'Puppet', 'Befunge', 'Gherkin', 'Lua', 'templ',
 'RouterOS Script', 'ANTLR', 'Astro', 'CUE', 'NewLisp', 'AIDL', 'MATLAB', 'Hack',
 'AMPL', 'EJS', 'PostScript', 'Emacs Lisp', 'Scala', 'QMake', 'Meson', 'Metal',
 'WGSL', 'Mako', 'Classic ASP', 'GLSL', 'jq', 'Fluent', 'Tcl', 'Svelte', 'Scheme',
 'Swift', 'UnrealScript', 'Racket', 'ASL', 'status', 'Apex', 'SystemVerilog',
 'ASP.NET', 'SRecode Template', 'Objective-C++', '1C Enterprise']

#dados do usuário com  a função
def get_user_data():
    event_watchs = st.sidebar.slider('event_watchs', 0.0, 1000.0, 500.0)
    event_forks = st.sidebar.slider('event_forks', 0.0, 1000.0, 500.0)
    event_issues = st.sidebar.slider('event_issues', 0.0, 1000.0, 500.0)
    event_projects = st.sidebar.slider('event_projects', 0, 1, 0)
    event_pages = st.sidebar.slider('event_pages', 0, 1, 0)
    event_discussions = st.sidebar.slider('event_discussions', 0, 1, 0)
    language_1 = st.sidebar.selectbox('Selecione a linguagem 1:', language1)
    language_2 = st.sidebar.selectbox('Selecione a linguagem 2:', language2)
    language_3 = st.sidebar.selectbox('Selecione a linguagem 3:', language3)

    
    

    user_data = {
        'event_watchs': event_watchs,
        'event_forks': event_forks,
        'event_issues': event_issues,
        'event_projects': event_projects,
        'event_pages': event_pages,
        'event_discussions': event_discussions,
        'language_1': language_1,
        'language_2': language_2,
        'language_3': language_3

    }

    features = pd.DataFrame(user_data, index=[0])

    return features

def switch_case(value):
    if value == 0:
        return "De 0 a 200 estrelas"
    elif value == 1:
        return "De 201 a 400 estrelas"
    elif value == 2:
        return "De 401 a 600 estrelas"
    elif value == 3:
        return "De 601 a 800 estrelas"
    elif value == 4:
        return "Mais de 801 estrelas"
    
user_input_variables = get_user_data()

#Grafico
#graf = st.bar_chart(user_input_variables)

st.subheader('Dados do usuário')
st.write(user_input_variables)

# Carregar o modelo salvo com pickle
with open('pipeline_modelo_definitivo.pkl', 'rb') as file:
    dtc = pickle.load(file)


#Previsao
prediction = dtc.predict(user_input_variables)

st.subheader('📊Previsão: ')
st.write(switch_case(prediction))