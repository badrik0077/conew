from flask import Flask

from app.API.views import api_blueprint
from app.views import post_blueprint
from exceptions.data_exceptions import DataSourceError
import config_logger

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
config_logger.config()


app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint, url_prefix='/api')




@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы не существует {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"Ошибка со стороны сервера {error}", 500



@app.errorhandler(DataSourceError)
def page_data_source_error(error):
    return f"Ошибка чтения данных", 500


if __name__ == '__main__':
    app.run()
