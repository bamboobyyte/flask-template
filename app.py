from website import init_app

if __name__ == '__main__':
    app = init_app()
    app.run(threaded=True, host='0.0.0.0')