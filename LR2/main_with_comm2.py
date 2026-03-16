import numpy as np
import matplotlib.pyplot as plt

def E(theta): 
    num = np.cos(k * l * np.cos(theta)) - np.cos(k * l)
    den = np.sin(theta)
    return num/den

def F(theta):
    return np.abs(E(theta)) / np.max(np.abs(E(theta)))

def Dmax(theta):
    mask = theta <= np.pi
    formula = (F(theta[mask])**2 * np.sin(theta[mask]))
    integral = np.trapezoid(formula, theta[mask])
    
    if integral <= 0:
        return 0
    return 4 / integral 
 
def D(theta): 
    dmax = Dmax(theta)
    if dmax <= 0:
        return np.zeros_like(theta)
    return F(theta)**2 * dmax

def creating_plot(d_times, d_dB, theta):
    fig, axs = plt.subplots(2, 2, figsize=(12,10), subplot_kw={'polar': False})
    fig.suptitle('D(θ)')

   
    theta_deg = np.degrees(theta)
    
    axs[0,0].plot(theta_deg, d_times, color='blue')
    axs[0,0].set_title("КНД (разы, декарт)")
    axs[0,0].set_xlabel("θ (град)")
    axs[0,0].set_ylabel("D(θ)")
    axs[0,0].grid(True)
    axs[0,0].set_xlim(0, 360)

    axs[0,1].plot(theta_deg, d_dB, color='red')
    axs[0,1].set_title("КНД (дБ, декарт)")
    axs[0,1].set_xlabel("θ (град)")
    axs[0,1].set_ylabel("D(θ) [дБ]")
    axs[0,1].grid(True)
    axs[0,1].set_xlim(0, 360)

    axs[1,0] = plt.subplot(2,2,3, polar=True)
    axs[1,0].plot(theta, d_times, color='blue')
    axs[1,0].set_title("КНД (разы, поляр)")
    axs[1,0].set_theta_zero_location('N')  
    axs[1,0].set_theta_direction(-1) 

    axs[1,1] = plt.subplot(2,2,4, polar=True)
    axs[1,1].plot(theta, d_dB, color='red')
    axs[1,1].set_title("КНД (дБ, поляр)")
    axs[1,1].set_theta_zero_location('N')
    axs[1,1].set_theta_direction(-1)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('var13.png')
    plt.show()


def main():
    global l, k
    f = 3.5 * 10 ** 9
    lmbd = 3 * 10 ** 8 / f
    l = 2.5 * lmbd / 2
    k = 2 * np.pi / lmbd
    theta = np.linspace(1e-9, 2 * np.pi - (1e-9), 4000)

    dmax_val = Dmax(theta=theta)
    print(f'{dmax_val:.3f} times\n{10 * np.log10(dmax_val):.3f} dB')
    
    d_times = D(theta)
    d_db = 10 * np.log10(d_times + 1e-9)
    
    creating_plot(d_times=d_times, d_dB=d_db, theta=theta)

    with open('python_results.txt', 'w', encoding='utf-8') as file:
        file.write('theta   d_times   d_db\n')
        for i in range(len(theta)):
            file.write(f'{theta[i]}   {d_times[i]}   {d_db[i]}\n')

if __name__=="__main__": 
    main()
