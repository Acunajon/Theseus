
"""
Jonathan Acuna
Fitting Function
"""
from functions import *
import numpy as np



CHI_LIST_NORM = []#                                                            CHI LIST NORM
NORM_LIST = []#                             PARAMETER   NORM                   NORM LIST
A_NORM_LIST = []#                                                              A LIST NORM

CHI_LIST_NORM_COLD = []#                                                       CHI LIST NORM COLD
NORM_COLD_LIST = []#                        PARAMETER   NORM COLD              NORM COLD LIST
A_NORM_COLD_LIST = []#                                                         A NORM COLD LIST

CHI_LIST_T_COLD = []#                                                          CHI LIST T COLD
T_COLD_LIST = []#                           PARAMETER   T COLD                 T COLD
A_T_COLD_LIST = []#                                                            A T COLD LIST

CHI_LIST_NORM_HOT = []#                                                        CHI LIST NORM HOT
NORM_HOT_LIST = []#                         PARAMETER   NORM HOT               NORM HOT LIST
A_NORM_HOT_LIST = []#                                                          A NORM HOT

CHI_LIST_T_HOT = []#                                                           T HOT CHI LIST
LIST_T_HOT = []#                            PARAMETER   T HOT                  T HOT LIST
A_T_HOT_LIST = []#                                                             A T HOT LIST









def fitting(wave, value, sigma, T_star, Norm=1, T_cold=100, Norm_cold=1, T_hot=100, Norm_hot=1, loop_num=1000):

    x = wave
    y = value
    z = sigma
    T_star = T_star
    Norm = Norm
    T_cold = T_cold
    Norm_cold = Norm_cold
    T_hot = T_hot
    Norm_hot = Norm_hot
    
    X = np.array(wave)
    Y = np.array(value)
    Z = np.array(sigma)
    
    result = []
    for i in x:
        Star = planck(i*1e-6, T_star)
        Cold = planck(i*1e-6)
        Hot = planck(i*1e-6)
        result.append(Star + Cold + Hot)
    Result = np.array(result)
    Chi = sum(((Result - Y)**2)/(Z**2))
    Re_Chi = Chi/(len(x)-4)

    loop = 0
    while loop < 100:
        loop += 1
 
    
        result = []#                                                               NORM
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi_Norm = sum(((Result - Y)**2)/(Z**2))
        Re_Chi_Norm = Chi_Norm/(len(x)-4)
    
    
        UP = 1.1
        DOWN = 0.9
        a = UP
        count = 0                                   
        while count < 10:                           
            count += 1
            Norm *= a
            NORM_LIST.append(Norm)
            result_loop_Norm = []#                                                 RESULT LIST
            for i in x[:10:]:                                       
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop_Norm.append(Star + Cold + Hot)
            X_ = np.array(x[:10:])
            Y_ = np.array(y[:10:])
            Z_ = np.array(z[:10:])
            Result_LOOP_NORM = np.array(result_loop_Norm)
            Chi_Norm = sum(((Result_LOOP_NORM - Y_)**2)/(Z_**2))
            Re_Chi_loop_Norm = Chi_Norm/(len(x)-4)
        
            if a == UP and Re_Chi_loop_Norm < Re_Chi_Norm:                
                a = UP
            elif a == UP and Re_Chi_loop_Norm > Re_Chi_Norm:
                a = DOWN
            elif a == DOWN and Re_Chi_loop_Norm < Re_Chi_Norm:
                a = DOWN
            elif a == DOWN and Re_Chi_loop_Norm > Re_Chi_Norm:
                a = UP
        
            CHI_LIST_NORM.append(Re_Chi_loop_Norm)
            A_NORM_LIST.append(a)
            Re_Chi_Norm = Re_Chi_loop_Norm 


    loop = 0
    while loop < 100:
        loop += 1
 
    
        result = []#                                                               NORM PRECISION
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi_Norm = sum(((Result - Y)**2)/(Z**2))
        Re_Chi_Norm = Chi_Norm/(len(x)-4)
    
    
        UP = 1.001
        DOWN = 0.999
        a = UP
        count = 0                                   
        while count < 10:                           
            count += 1
            Norm *= a
            NORM_LIST.append(Norm)
            result_loop_Norm = []#                                                 RESULT LIST
            for i in x[:10:]:                                       
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop_Norm.append(Star + Cold + Hot)
            X_ = np.array(x[:10:])
            Y_ = np.array(y[:10:])
            Z_ = np.array(z[:10:])
            Result_LOOP_NORM = np.array(result_loop_Norm)
            Chi_Norm = sum(((Result_LOOP_NORM - Y_)**2)/(Z_**2))
            Re_Chi_loop_Norm = Chi_Norm/(len(x)-4)
        
            if a == UP and Re_Chi_loop_Norm < Re_Chi_Norm:                
                a = UP
            elif a == UP and Re_Chi_loop_Norm > Re_Chi_Norm:
                a = DOWN
            elif a == DOWN and Re_Chi_loop_Norm < Re_Chi_Norm:
                a = DOWN
            elif a == DOWN and Re_Chi_loop_Norm > Re_Chi_Norm:
                a = UP
        
            CHI_LIST_NORM.append(Re_Chi_loop_Norm)
            A_NORM_LIST.append(a)
            Re_Chi_Norm = Re_Chi_loop_Norm 

            
    loop_Norms = 0
    while loop_Norms < 100:
        loop_Norms += 1


        result = []#                                                               NORM COLD
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)
        
        UP = 1.1
        DOWN = 0.9
        a = UP
        count = 0                                  
        while count < 10:                            
            count += 1
            Norm_cold *= a
            NORM_COLD_LIST.append(Norm_cold)
            result_loop_Norm_cold = []#                                            RESULT LIST NORM COLD
            for i in x:                                      
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop_Norm_cold.append(Star + Cold + Hot)
            Result = np.array(result_loop_Norm_cold)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:                
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
    
            CHI_LIST_NORM_COLD.append(Re_Chi_loop)
            A_NORM_COLD_LIST.append(a)
            Re_Chi = Re_Chi_loop
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------       
        result = []#                                                               NORM HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)

        UP = 1.1
        DOWN = 0.9
        a = UP
        count = 0
        while count < 10:
            count += 1
            Norm_hot *= a
            NORM_HOT_LIST.append(Norm_hot)
            result_loop = []#                                                      RESULT NORM HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:               
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
    
            CHI_LIST_NORM_HOT.append(Re_Chi_loop)
            A_NORM_HOT_LIST.append(a)
            Re_Chi = Re_Chi_loop   
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
    T_loop = 0
    while T_loop < 100:
        T_loop += 1       
        
        
        result = []#                                                               T HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)

        UP = 1.1
        DOWN = 0.9
        a = UP
        count = 0
        while count < 10:
            count += 1
            T_cold *= a
            T_COLD_LIST.append(T_cold)
            result_loop = []#                                                      RESULT T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
        
            A_T_COLD_LIST.append(a)
            CHI_LIST_T_COLD.append(Re_Chi_loop)
            Re_Chi = Re_Chi_loop 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
        result = []#                                                               T HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)

        UP = 1.1
        DOWN = 0.9
        a = UP
        count = 0
        while count < 10:
            count += 1
            T_hot *= a
            LIST_T_HOT.append(T_hot)
            result_loop = []#                                                      RESULT T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
       
            A_T_HOT_LIST.append(a)
            CHI_LIST_T_HOT.append(Re_Chi_loop)
            Re_Chi = Re_Chi_loop 
        

#                       LOOP 2 FOR Precision
    loop_2 = 0
    while loop_2 < 200:
        loop_2 += 1                        

       
        result = []#                                                               NORM COLD
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)
        
        UP = 1.01
        DOWN = 0.99
        a = UP
        count = 0                                  
        while count < 10:                            
            count += 1
            Norm_cold *= a
            NORM_COLD_LIST.append(Norm_cold)
            result_loop_Norm_cold = []#                                            RESULT LIST NORM COLD
            for i in x:                                      
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop_Norm_cold.append(Star + Cold + Hot)
            Result = np.array(result_loop_Norm_cold)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:                
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
    
            CHI_LIST_NORM_COLD.append(Re_Chi_loop)
            A_NORM_COLD_LIST.append(a)
            Re_Chi = Re_Chi_loop
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------       
        result = []#                                                               NORM HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)

        UP = 1.01
        DOWN = 0.99
        a = UP
        count = 0
        while count < 10:
            count += 1
            Norm_hot *= a
            NORM_HOT_LIST.append(Norm_hot)
            result_loop = []#                                                      RESULT NORM HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:               
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
    
            CHI_LIST_NORM_HOT.append(Re_Chi_loop)
            A_NORM_HOT_LIST.append(a)
            Re_Chi = Re_Chi_loop   
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
    T_loop_2 = 0
    while T_loop_2 < 100:
        T_loop_2 += 1       
        
        
        result = []#                                                               T HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)

        UP = 1.01
        DOWN = 0.99
        a = UP
        count = 0
        while count < 10:
            count += 1
            T_cold *= a
            T_COLD_LIST.append(T_cold)
            result_loop = []#                                                      RESULT T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
        
            A_T_COLD_LIST.append(a)
            CHI_LIST_T_COLD.append(Re_Chi_loop)
            Re_Chi = Re_Chi_loop 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
        result = []#                                                               T HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result.append(Star + Cold + Hot)
        Result = np.array(result)
        Chi = sum(((Result - Y)**2)/(Z**2))
        Re_Chi = Chi/(len(x)-4)
        
        UP = 1.01
        DOWN = 0.99
        a = UP
        count = 0
        while count < 10:
            count += 1
            T_hot *= a
            LIST_T_HOT.append(T_hot)
            result_loop = []#                                                      RESULT T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result_loop.append(Star + Cold + Hot)
            Result = np.array(result_loop)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            Re_Chi_loop = Chi_Norm/(len(x)-4)

            if a == UP and Re_Chi_loop < Re_Chi:
                a = UP
            elif a == UP and Re_Chi_loop > Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop < Re_Chi:
                a = DOWN
            elif a == DOWN and Re_Chi_loop > Re_Chi:
                a = UP
       
            A_T_HOT_LIST.append(a)
            CHI_LIST_T_HOT.append(Re_Chi_loop)
            Re_Chi = Re_Chi_loop 
         
     

            
    Loop_3 = 0
    while Loop_3 < loop_num:
        Loop_3 += 1
        print Loop_3
    
        UP = 1.01
        DOWN = 0.99
    
        if Loop_3 > 200 and Loop_3 <= 400:
            UP = 1.001
            DOWN = 0.999
        elif Loop_3 > 400 and Loop_3 <= 600:
            UP = 1.0001
            DOWN = 0.9999
        elif Loop_3 > 600 and Loop_3 <= 800:
            UP = 1.00001
            DOWN = 0.99999
        elif Loop_3 > 800:
            UP = 1.000001
            DOWN = 0.999999
    
    
    
    
    
        loop_2 = 0
        while loop_2 < 100:
            loop_2 += 1                          

        

    
            result = []#                                                               NORM
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result.append(Star + Cold + Hot)
            Result = np.array(result)
            Chi_Norm = sum(((Result - Y)**2)/(Z**2))
            RE_CHI_NORM = Chi_Norm/(len(x)-4)
    
    
            a = UP
            count = 0                                   
            while count < 10:                           
                count += 1
                Norm *= a
                NORM_LIST.append(Norm)
                result_loop = []#                                                      RESULT NORM HOT
                for i in x:
                    Star = planck(i*1e-6, T_star, Norm)
                    Cold = planck(i*1e-6, T_cold, Norm_cold)
                    Hot = planck(i*1e-6, T_hot, Norm_hot)
                    result_loop.append(Star + Cold + Hot)
                Result = np.array(result_loop)
                Chi_Norm = sum(((Result - Y)**2)/(Z**2))
                Re_Chi_loop_Norm = Chi_Norm/(len(x)-4)

                if a == UP and Re_Chi_loop_Norm < Re_Chi:               
                    a = UP
                elif a == UP and Re_Chi_loop_Norm > Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop_Norm < Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop_Norm > Re_Chi:
                    a = UP
        
                CHI_LIST_NORM.append(Re_Chi_loop_Norm)
                A_NORM_LIST.append(a)
                RE_CHI_NORM = Re_Chi_loop_Norm 
        
            
            
            result = []#                                                               NORM COLD
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result.append(Star + Cold + Hot)
            Result = np.array(result)
            Chi = sum(((Result - Y)**2)/(Z**2))
            Re_Chi = Chi/(len(x)-4)


            a = UP
            count = 0                                  
            while count < 10:                            
                count += 1
                Norm_cold *= a
                NORM_COLD_LIST.append(Norm_cold)
                result_loop_Norm_cold = []#                                            RESULT LIST NORM COLD
                for i in x:                                      
                    Star = planck(i*1e-6, T_star, Norm)
                    Cold = planck(i*1e-6, T_cold, Norm_cold)
                    Hot = planck(i*1e-6, T_hot, Norm_hot)
                    result_loop_Norm_cold.append(Star + Cold + Hot)
                Result = np.array(result_loop_Norm_cold)
                Chi_Norm = sum(((Result - Y)**2)/(Z**2))
                Re_Chi_loop = Chi_Norm/(len(x)-4)
        
                if a == UP and Re_Chi_loop < Re_Chi:                
                    a = UP
                elif a == UP and Re_Chi_loop > Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop < Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop > Re_Chi:
                    a = UP
    
                CHI_LIST_NORM_COLD.append(Re_Chi_loop)
                A_NORM_COLD_LIST.append(a)
                Re_Chi = Re_Chi_loop
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------       
            result = []#                                                               NORM HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result.append(Star + Cold + Hot)
            Result = np.array(result)
            Chi = sum(((Result - Y)**2)/(Z**2))
            Re_Chi = Chi/(len(x)-4)


            a = UP
            count = 0
            while count < 10:
                count += 1
                Norm_hot *= a
                NORM_HOT_LIST.append(Norm_hot)
                result_loop = []#                                                      RESULT NORM HOT
                for i in x:
                    Star = planck(i*1e-6, T_star, Norm)
                    Cold = planck(i*1e-6, T_cold, Norm_cold)
                    Hot = planck(i*1e-6, T_hot, Norm_hot)
                    result_loop.append(Star + Cold + Hot)
                Result = np.array(result_loop)
                Chi_Norm = sum(((Result - Y)**2)/(Z**2))
                Re_Chi_loop = Chi_Norm/(len(x)-4)

                if a == UP and Re_Chi_loop < Re_Chi:               
                    a = UP
                elif a == UP and Re_Chi_loop > Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop < Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop > Re_Chi:
                    a = UP
    
                CHI_LIST_NORM_HOT.append(Re_Chi_loop)
                A_NORM_HOT_LIST.append(a)
                Re_Chi = Re_Chi_loop
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------    
        T_loop_2 = 0
        while T_loop_2 < 100:
            T_loop_2 += 1        
            
        
            result = []#                                                               T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result.append(Star + Cold + Hot)
            Result = np.array(result)
            Chi = sum(((Result - Y)**2)/(Z**2))
            Re_Chi = Chi/(len(x)-4)


            a = UP
            count = 0
            while count < 10:
                count += 1
                T_cold *= a
                T_COLD_LIST.append(T_cold)
                result_loop = []#                                                      RESULT T HOT
                for i in x:
                    Star = planck(i*1e-6, T_star, Norm)
                    Cold = planck(i*1e-6, T_cold, Norm_cold)
                    Hot = planck(i*1e-6, T_hot, Norm_hot)
                    result_loop.append(Star + Cold + Hot)
                Result = np.array(result_loop)
                Chi_Norm = sum(((Result - Y)**2)/(Z**2))
                Re_Chi_loop = Chi_Norm/(len(x)-4)

                if a == UP and Re_Chi_loop < Re_Chi:
                    a = UP
                elif a == UP and Re_Chi_loop > Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop < Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop > Re_Chi:
                    a = UP
        
                A_T_COLD_LIST.append(a)
                CHI_LIST_T_COLD.append(Re_Chi_loop)
                Re_Chi = Re_Chi_loop 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
            result = []#                                                               T HOT
            for i in x:
                Star = planck(i*1e-6, T_star, Norm)
                Cold = planck(i*1e-6, T_cold, Norm_cold)
                Hot = planck(i*1e-6, T_hot, Norm_hot)
                result.append(Star + Cold + Hot)
            Result = np.array(result)
            Chi = sum(((Result - Y)**2)/(Z**2))
            Re_Chi = Chi/(len(x)-4)


            a = UP
            count = 0
            while count < 10:
                count += 1
                T_hot *= a
                LIST_T_HOT.append(T_hot)
                result_loop = []#                                                      RESULT T HOT
                for i in x:
                    Star = planck(i*1e-6, T_star, Norm)
                    Cold = planck(i*1e-6, T_cold, Norm_cold)
                    Hot = planck(i*1e-6, T_hot, Norm_hot)
                    result_loop.append(Star + Cold + Hot)
                Result = np.array(result_loop)
                Chi_Norm = sum(((Result - Y)**2)/(Z**2))
                Re_Chi_loop = Chi_Norm/(len(x)-4)
            
                if a == UP and Re_Chi_loop < Re_Chi:
                    a = UP
                elif a == UP and Re_Chi_loop > Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop < Re_Chi:
                    a = DOWN
                elif a == DOWN and Re_Chi_loop > Re_Chi:
                    a = UP
       
                A_T_HOT_LIST.append(a)
                CHI_LIST_T_HOT.append(Re_Chi_loop)
                Re_Chi = Re_Chi_loop 
                
    result = []
    for i in x:
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        result.append(Star + Cold + Hot)
    Result = np.array(result)
    Chi = sum(((Result - Y)**2)/(Z**2))
    Re_Chi = Chi/(len(x)-4)            
                
                
    return Norm, T_cold, Norm_cold, T_hot, Norm_hot, Re_Chi