import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import tempfile

from entities import Image
from core import locate

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route('/images', methods = ['POST'])
def upload_file():
    image = request.files['image']
    query_image = request.files['queryImage']


    # create a temporary directory
    with tempfile.TemporaryDirectory() as directory:
        filename = secure_filename(image.filename)
        image.save(os.path.join(directory, filename))
        query_filename = secure_filename(query_image.filename)
        query_image.save(os.path.join(directory, query_filename))


        image = Image(os.path.join(directory, filename))
        template = Image(os.path.join(directory, query_filename), cluster=image.cluster)

        max_contribution, max_offset = locate(image, template)

        return dict(location=max_offset, score=max_contribution)
    # use this in order to skip the save part
    # # read image file string data
    # filestr = request.files['file'].read()
    # # convert string data to numpy array
    # npimg = numpy.fromstring(filestr, numpy.uint8)
    # # convert numpy array to image
    # img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

		
if __name__ == '__main__':
   app.run(debug = True)