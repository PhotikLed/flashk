from flask import Flask

app = Flask(__name__)


@app.route('/carousel')
def photos():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
                    crossorigin="anonymous">                    
                    <title>Пожилые меркедес бендз</title>
                  </head>
                  <body>
                    <h1>Фотогалерея меркедес бендз</h1>
                    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="static/img/1.jpg" class="d-block w-100" alt="меркедес № 1">
                        </div>
                        <div class="carousel-item">
                          <img src="static/img/2.jpg" class="d-block w-100" alt="меркедес № 4">
                        </div>
                        <div class="carousel-item">
                          <img src="static/img/3.jpg" class="d-block w-100" alt="меркедес № 3">
                        </div>
                        <div class="carousel-item">
                          <img src="static/img/4.jpg" class="d-block w-100" alt="меркедес № 4">
                        </div>
                      </div>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
