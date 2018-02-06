# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:23:05 2017

@author: G30
"""

import tensorflow as tf
#import keras.backend as K


def get_session(process_no):
    '''
    config = tf.ConfigProto()
    process_no=float(process_no)
    config.gpu_options.per_process_gpu_memory_fraction = (0.7/process_no)
    sess = tf.Session(config=config)
    K.set_session(sess)
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    '''
    sess = tf.Session()
    return sess
