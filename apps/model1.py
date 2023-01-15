import streamlit as st
import pickle
from PIL import Image
from keras.models import load_model
import numpy as np
import joblib
import sklearn
import warnings
warnings.filterwarnings("ignore")



results = {}

def open_image(imageName):
    image = Image.open("images/"+imageName)
    st.image(image, use_column_width=True, clamp=255)

def open_image_small(imageName):
    image = Image.open("images/"+imageName)
    st.image(image, width=400, clamp=255)

def run(df_clf, df_reg):
    # -----------------------------------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Classification Models</p>', unsafe_allow_html=True)
    st.markdown('To predict either customer will buy drinks.')

    # -----------------------------------------------------------------------------------------------
    st.markdown('#### Random Forest Model')

    rf_model = pickle.load(open(f'models/best_rf_model.pkl','rb'))

    st.markdown("**Predicted result**")
    rf_pred = rf_model.predict(df_clf)

    if rf_pred == 1:
        st.success('Buy Drink')
    else:
        st.success('Not Buy Drink')

    st.markdown('##### The training and testing phrase of this model')
    st.text("")

    st.markdown("**The best hyperparameters**")
    st.info("{'m__criterion': 'gini','m__max_depth': None,'m__max_features': 'sqrt','m__n_estimators': 110}")

    st.markdown("**Result of rf model after hyperparameters and tuning**")
    open_image_small('rf_model_matrix.png')

    st.markdown("**Receiver Operating Characteristic (ROC) Curve**")
    open_image('rf_model_roc.png')

    st.markdown("**Precision-Recall Curve**")
    open_image('rf_model_prc.png')

    
    

    # -----------------------------------------------------------------------------------------------
    st.markdown('#### K-Nearest Neighbour (KNN)')

    knn_model = pickle.load(open(f'models/best_knn_model.pkl','rb'))
    
    st.markdown("**Predicted result**")
    knn_pred = knn_model.predict(df_clf)

    if knn_pred == 1:
        st.success('Buy Drink')
    else:
        st.success('Not Buy Drink')

    st.markdown('##### The training and testing phrase of this model')
    st.text("")

    st.markdown("**The best hyperparameters**")
    st.info("{'m__metric': 'euclidean', 'm__n_neighbors': 13, 'm__weights': 'uniform'}")

    st.markdown("**Result of rf model after hyperparameters and tuning**")
    open_image_small('knn_model_matrix.png')

    st.markdown("**Receiver Operating Characteristic (ROC) Curve**")
    open_image('knn_model_roc.png') 

    st.markdown("**Precision-Recall Curve**")
    open_image('knn_model_prc.png') 



    # -----------------------------------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Ensemble - Stacking all classification models</p>', unsafe_allow_html=True)
    st.markdown('To compare the results of individual machine learning model with ensemble models')

    #stacking_model = pickle.load(open(f'stacking_model.pkl','rb'))
    stacking_model = joblib.load("models/stacking_model.pkl")
    
    st.markdown("**Predicted result**")
    stack_pred = stacking_model.predict(df_clf)

    if stack_pred == 1:
        st.success('Buy Drink')
    else:
        st.success('Not Buy Drink')

    st.success("Ensemble Model Prediction Successfully") 

    code = '''def get_stacking():
        level0 = list()
        level0.append(('knn', KNeighborsClassifier()))
        level0.append(('rf', RandomForestClassifier()))    
       
        level1 = KNeighborsClassifier()     
        model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)
         
        return model'''
    st.code(code, language='python')

    st.text("")
    st.markdown("**Models performance for comparison - based on f1-score**")
    open_image('stacking_model_performance.png')


    # -----------------------------------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Deep Learning - Neural Network</p>', unsafe_allow_html=True)

    st.markdown('To compare the results other machine learning classification models')
    neural_model = load_model('models/neural.h5')

    st.markdown("**Predicted result**")
    neural_pred = neural_model.predict(np.asarray(df_clf).astype('float32'))
    if neural_pred[0] > 0.5:
        st.success('Buy Drink')
    else:
        st.success('Not Buy Drink')

    st.markdown('##### The training and testing phrase of this model')
    st.text("")
    
    st.markdown("**Summary of the model**")
    open_image_small('nn_summary.png')
    st.text("")
    st.markdown("**History - Accuracy vs Epochs**")
    open_image('nn_epoch.png')

    
    

    # -----------------------------------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Regression</p>', unsafe_allow_html=True)
    st.markdown('**To predict the revenue (total spent) of customer.**') 

    # -----------------------------------------------------------------------------------------------
    st.markdown('#### Support Vector Regression (SVR)')

    svr_model = pickle.load(open(f'models/svr_model.pkl','rb'))
    
    st.markdown("**Predicted result**")
    svr_pred = svr_model.predict(df_reg)
    st.success(svr_pred) 

    st.markdown('##### The training and testing phrase of this model')
    st.text("")
    st.markdown("**The best hyperparameters**")
    st.info("{'C': 0.1, 'gamma': 0.01, 'kernel': 'rbf'}")

    st.markdown("**Result of SVR model after hyperparameters**")
    st.info("MSE: 3.613073176576472")

    # -----------------------------------------------------------------------------------------------
    st.markdown('#### Linear Regression (LR)')

    lr_model = pickle.load(open(f'models/ridge_model.pkl','rb'))
    
    st.markdown("**Predicted result**")
    lr_pred = lr_model.predict(df_reg)
    st.success(lr_pred) 

    st.markdown('##### The training and testing phrase of this model')
    st.text("")
    st.markdown("**The best hyperparameters**")
    st.info("{'alpha': 100, 'fit_intercept': True, 'normalize': True}")

    st.markdown("**Result of SVR model after hyperparameters**")
    st.info("MSE: 3.620864736367097")

    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Comparisons</p>', unsafe_allow_html=True)
    st.markdown('#### Comparison Between Classification ROC')
    open_image('rf_knn_roc_comparison.png')

    st.markdown('#### Comparison Between Classification PRC')
    open_image('rf_knn_prc_comparison.png')

    st.markdown('#### Comparison Between Classification Hypertuning Result')
    open_image('hypertuning_models.png')

    st.text("")
    st.markdown('#### Comparison Between Buy Drink Result')
    open_image('buy_drink_comparison.png')

    st.text("")
    st.markdown('#### Comparison Between Regression Model')
    open_image('buy_drink_comparison.png')


    

    return 'models'

