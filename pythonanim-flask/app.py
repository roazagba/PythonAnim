from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import sys
import io
import ast

app = Flask(__name__)
CORS(app)

@app.route('/execute', methods=['POST'])
def execute_code():
    if not request.json or 'code' not in request.json:
        return jsonify({'error': 'Aucun code fourni'}), 400

    code = request.json['code']
    output = ''
    
    unsafe_functions = ['input', 'eval', 'exec', 'open', 'compile']
    unsafe_modules = ['os', 'sys', 'subprocess', 'shutil', 'ctypes', 'socket', 'ftplib', 'http', 'urllib', 'pickle', 'marshal', 'functools ', 'signal', 'tempfile', 'resource', 'importlib', 'inspect', 'socketserver', 'paramiko ', 'pysftp', ]

    
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in unsafe_functions:
                    return jsonify({
                        'error': f"Erreur: La fonction '{func_name}()' est utilisée dans le code. Elle ne doit pas être utilisée. Merci."
                    }), 400
            
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    module_name = alias.name.split('.')[0]
                    if module_name in unsafe_modules:
                        return jsonify({
                            'error': f"Erreur: Le module '{module_name}' est importé. Il ne doit pas être utilisé. Merci."
                        }), 400
            
            elif isinstance(node, ast.ImportFrom):
                module_name = node.module.split('.')[0] if node.module else ''
                if module_name in unsafe_modules:
                    return jsonify({
                        'error': f"Erreur: Le module '{module_name}' est importé. Il ne doit pas être utilisé. Merci."
                    }), 400
                    
    except Exception:
        exc_type, exc_value, exc_tb = sys.exc_info()
        formatted_lines = traceback.format_exception(exc_type, exc_value, exc_tb)
        cleaned_lines = [line for line in formatted_lines if 'File "' not in line]
        error = ''.join(cleaned_lines)
        return jsonify({'error': f'Erreur de syntaxe dans le code: {error}'}), 400
    
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code, globals())
        output = sys.stdout.getvalue()
    except Exception:
        exc_type, exc_value, exc_tb = sys.exc_info()
        formatted_lines = traceback.format_exception(exc_type, exc_value, exc_tb)
        cleaned_lines = [line for line in formatted_lines if 'File "' not in line]
        error = ''.join(cleaned_lines)
        return jsonify({'error': f'Erreur de syntaxe dans le code: {error}'}), 400
    finally:
        sys.stdout = old_stdout

    result = {
        'code' : code,
        'output': output,
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
