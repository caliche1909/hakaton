from config import Config
form src import app

configurations = config['development']
app= init_app(configuration)

if __name__ == '__main__':
    app.run()