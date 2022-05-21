from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


from App.model.pessoas.pessoa import Pessoa
from App.model.refeicao import Refeicao
from App.model.dieta import Dieta
from App.model.itemdieta import ItemDieta
from App.model.alimentos import Alimentos
from App.model.atleta import Atleta
from App.model.metaatleta import Metaatleta
from App.model.unalimento import Unalimento





class PessoaSchema(ModelSchema):
    class Meta:
        model = Pessoa



class RefeicaoSchema(ModelSchema):
    class Meta:
        model = Refeicao
    #pessoa = fields.Nested(PessoaSchema)

class UnAlimentoSchema(ModelSchema):
    class Meta:
        model = Unalimento

class AlimentoSchema(ModelSchema):
    class Meta:
        model = Alimentos

    unalimento = fields.Nested(UnAlimentoSchema)

class ItemDietaSchema(ModelSchema):
    class Meta:
        model = ItemDieta
    #dieta = fields.Nested('DietaSchema',only=('id','descricao','data',))
    alimento = fields.Nested('AlimentoSchema',only=('id','descricao','unalimento'))


class PessoaSchema(ModelSchema):
    class Meta:
        model = Pessoa
    refeicao =fields.Nested(RefeicaoSchema,many=True)

class PessoaClienteRefeicoesSchema(ModelSchema):
    class Meta:
        model = Pessoa

    refeicao = fields.Nested(RefeicaoSchema(many=True),exclude=('pessoa',),dump_only=True)
 



class UnFoodsSchema(ModelSchema):
    class Meta:
        model = Unalimento



class Atletaschema(ModelSchema):
    class Meta:
        model = Atleta


class FoodsSchema(ModelSchema):
    class Meta:
        model = Alimentos

    pessoa = fields.Nested(Atletaschema)
    unalimento = fields.Nested(UnFoodsSchema)

class MetaAtletaschema(ModelSchema):
    class Meta:
        model = Metaatleta

    exclude = ('atleta',)



class DietaSchema(ModelSchema):
    class Meta:
        model = Dieta

    dieta_refeicao = fields.Nested(RefeicaoSchema)
    metaatleta = fields.Nested(MetaAtletaschema)

