from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__, template_folder='.', static_folder='.')


PRODUCTS_DB = {
    1: {"name": "Ração Premium Cães Adultos 1kg", "price": 29.90, "desc": "Sabor Carne e Vegetais"},
    2: {"name": "Sachê Whiskas Gatos Carne 85g", "price": 4.50, "desc": "Para gatos castrados"},
    3: {"name": "Brinquedo Mordedor Osso de Borracha", "price": 18.90, "desc": "Alta durabilidade"},
    4: {"name": "Shampoo Pet Estética Neutro 500ml", "price": 24.99, "desc": "Fragrância suave e hipoalergênico"},
    5: {"name": "Arranhador para Gatos Torre Classic", "price": 89.90, "desc": "Com plataforma de descanso"}
}



@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):

    product = PRODUCTS_DB.get(product_id)
    if product:
        return jsonify({
            "success": True, 
            "product": product
        }), 200
        
    return jsonify({
        "success": False, 
        "message": "Produto não encontrado!"
    }), 404


@app.route('/api/checkout', methods=['POST'])
def checkout():

    data = request.get_json(silent=True) or {}
    
    cpf = data.get('cpf', 'Não informado')
    total = data.get('total', 0.0)
    payment_method = data.get('payment_method', 'Desconhecido')

    auth_code = str(random.randint(100000, 999999))
    
    return jsonify({
        "success": True,
        "auth_code": auth_code,
        "message": f"Pagamento via {payment_method.upper()} processado com sucesso!"
    }), 200


if __name__ == '__main__':
    print("*" * 50)
    print("  SERVIDOR DO TOTEM DO PETSHOP INICIADO (Porta 5000)  ")
    print("*" * 50)
    app.run(debug=True, port=5000)