from flask import jsonify
from flask_api import status

def okJson(obj):
    return jsonify(obj), status.HTTP_200_OK

def conflictAccountExists():
    return jsonify({'error':'Account exists for that email'}), status.HTTP_409_CONFLICT

def okNoContent():
    return '', status.HTTP_204_NO_CONTENT

def unauthorized():
    return '', status.HTTP_401_UNAUTHORIZED

def forbidden():
    return '', status.HTTP_403_FORBIDDEN

def heresYourToken(token):
    return jsonify({'token':token}), status.HTTP_200_OK

def heresYourTags(tags):
    return jsonify({'tags':tags}), status.HTTP_200_OK