import numpy as np
import pickle


class hpp():
    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open('model.pickle','rb') as file:
            self.model = pickle.load(file)

    def predict(self):

        self.load_model()   # above fuction call kele aahe

        size= float(self.data['size'])
        total_sqft= float(self.data['total_sqft'])
        bath= float(self.data['bath'])
        balcony= float(self.data['balcony'])
        New_area_type= float(self.data['New_area_type'])
    
       

        array = np.array([size, total_sqft,bath, balcony, New_area_type],ndmin = 2)
        print(array)
        print("*"*50)

        res = np.round(self.model.predict(array),2)[0]    # yethe ans he array([33.5]) ase yete so aatil list [33.5] yachi index 0 aahe so we give [0]
        print(res)	    
        return res


# ha part only testing perpose sathi aahe ha always run nahi hote
# if __name__ == "__main__":
#     data = {
#         'CRIM': 0.21,
#         'ZN':0.01,
#         'INDUS' : 15.89000,
#         'CHAS' : 2.00000,
#         'NOX' :0.75000,
#         'RM':7.95100,
#         'AGE':85.80000,
#         'DIS': 2.58930,
#         'RAD':3.00000,
#         'TAX':250.00000,
#         'PTRATIO':12.40000,
#         'B':350.90000,
#         'LSTAT':15.92000
#     }

#     hpp_obj = hpp(data)

#     hpp_obj.predict()
