from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pyngrok import ngrok
# from bayesianbandits import Arm, NormalInverseGammaRegressor, Agent, ThompsonSampling, ContextualAgent
# from gtts import gTTS
import os
import numpy as np
import time
import requests
import json
# from collections import deque
from datetime import datetime