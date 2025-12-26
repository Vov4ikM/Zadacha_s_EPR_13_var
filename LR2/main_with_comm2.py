import numpy as np
import matplotlib.pyplot as plt

def E(theta): #Нахождение напряжённости элек.поля, там ещё оно номрмированно, т.к. сокращая при этом параметры некоторые
    num = np.cos(k * l * np.cos(theta)) - np.cos(k * l)
    den = np.sin(theta)
    return num/den

def F(theta):
    return abs(E(theta)) / abs(E(theta).max())

def Dmax(theta):
    formula = (F(theta)**2 * np.sin(theta))
    return 2 / np.trapezoid(formula, theta) #Трапецоида = интеграл по theta
 
def D(theta): #Формула нахождения КНД
    return F(theta)**2 * Dmax(theta)

def creating_plot(d_times, d_dB, theta):

    fig, axs = plt.subplots(2, 2, figsize=(12,10), subplot_kw={'polar': False})
    fig.suptitle('D(θ)')

    axs[0,0].plot(theta, d_times, color='blue')
    axs[0,0].set_title("КНД (разы, декарт)")
    axs[0,0].set_xlabel("θ (рад)")
    axs[0,0].set_ylabel("D(θ)")
    axs[0,0].grid(True)

    axs[0,1].plot(theta, d_dB, color='red')
    axs[0,1].set_title("КНД (дБ, декарт)")
    axs[0,1].set_xlabel("θ (рад)")
    axs[0,1].set_ylabel("D(θ) [дБ]")
    axs[0,1].grid(True)

    axs[1,0] = plt.subplot(2,2,3, polar=True)
    axs[1,0].plot(theta, d_times, color='blue')
    axs[1,0].set_title("КНД (разы, поляр)")

    axs[1,1] = plt.subplot(2,2,4, polar=True)
    axs[1,1].plot(theta, d_dB, color='red')
    axs[1,1].set_title("КНД (дБ, поляр)")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('var13.png')
    plt.show()


def main():
    global l, k
    f = 3.5 * 10 ** 9
    lmbd = 3 * 10 ** 8 / f
    l = 2.5 * lmbd / 2
    k = 2 * np.pi / lmbd
    theta = np.linspace(1e-9, np.pi-(1e-9), 2000)

    print(f'{Dmax(theta=theta):.3f} times\n{10 * np.log10(Dmax(theta=theta)):.3f} dB') # .3f - форматирование чисел с плавающей точкой, до 3х символов после запятой
    
    creating_plot(d_times=D(theta), d_dB=10*np.log10(D(theta) + 1e-9), theta=theta) # 10*np.log() - перевод из d_times в дециБеллы
    d_times = D(theta)
    d_db = 10*np.log10(D(theta) + 1e-9)

    with open('python_results.txt', 'w', encoding='utf-8') as file: #Запись в файл данные
        file.write('theta   d_times   d_db\n')
        for i in range(len(theta)):
            file.write(f'{theta[i]}   {d_times[i]}   {d_db[i]}\n')

if __name__=="__main__": 
    main()
