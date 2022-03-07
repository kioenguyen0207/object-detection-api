from distutils.command.build_scripts import first_line_re
from flask import Flask, request, jsonify, send_file
from flask_restful import Api, Resource, reqparse
import werkzeug
import os
import glob
import subprocess
import time

from imagekit_module import *
from helper import *

FILE_PATH = "detector/temp"

class detector(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
            args = parser.parse_args()
            uploaded_file = args['file']
            working_file = os.path.join(FILE_PATH, "temp" + uploaded_file.filename[-4:])
            # working_file = os.path.join(FILE_PATH, uploaded_file.filename)
            uploaded_file.save(working_file)
            #detect
            command = f"python detector/yolo_image.py -i {working_file} -o {working_file} -t 0.3"
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            p_status = proc.wait()
            with open('detector/temp/temp.txt', 'r') as f:
                content_list = f.readlines()
            converted_list = []
            for element in content_list:
                converted_list.append(element.strip())
            url = uploadimg(working_file)
            return jsonify({
                'url' : f'{url}',
                'status': verify_classes(converted_list),
                'classes': converted_list
            })
        except Exception as ex:
            return jsonify({"msg": ex})