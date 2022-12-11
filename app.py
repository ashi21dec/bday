import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import io
import base64
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.image as mpimg


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
