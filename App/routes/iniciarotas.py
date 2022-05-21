from App import app
from App.routes.routesmetaatleta import routesmetaatleta
from App.routes.routestabalimentos import routestabalimentos
from App.routes.routesrefeicao import routesrefeicao
from App.routes.routesdieta import routesdieta
from App.routes.routespessoa import routespessoa
from App.routes.routesunalimento import routesunalimentos
from App.routes.routesmetaatleta import routesmetaatleta
from App.routes.routesatleta import routesatleta
from App.routes.routesseveral import routesseveral



def estabelecerotas():
    app.register_blueprint(routesatleta)
    app.register_blueprint(routesmetaatleta)
    app.register_blueprint(routesunalimentos)
    app.register_blueprint(routespessoa)
    app.register_blueprint(routesdieta)
    app.register_blueprint(routesrefeicao)
    app.register_blueprint(routestabalimentos)
    app.register_blueprint(routesmetaatleta)
    app.register_blueprint(routesseveral)


