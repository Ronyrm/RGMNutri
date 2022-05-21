from flask import Blueprint
from App.views.refeicao import *
routesrefeicao = Blueprint('routesrefeicao',__name__)

@routesrefeicao.route('/post/refeicao',methods=['POST'])
def postrefeicao():
    return post_refeicao()



@routesrefeicao.route('/get/refeicao/atleta', methods=['GET'])
def getrefeicaoatleta():
    return get_refeicao_atleta()

@routesrefeicao.route('/del/refeicao/atleta/<id>')
def deleterefeicao(id):
    return delete_refeicao(id)