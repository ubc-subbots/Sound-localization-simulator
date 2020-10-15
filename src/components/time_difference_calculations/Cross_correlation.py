import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


class Cross_correlation:
    def __init__(self):
        pass
    
    #lag finder
    def lag_finder(self, y1, y2, sample_rate):
        n = len(y1)+len(y2)-1
        
        #cross_correlation = signal.correlate(y2, y1, mode='full') / np.sqrt(signal.correlate(y1, y1, mode='full')[int(n/2)] * signal.correlate(y2, y2, mode='full')[int(n/2)])
        cross_correlation = signal.correlate(y2, y1, mode='full')
        delay_range = np.linspace( (-0.5*n/sample_rate), (0.5*n/sample_rate), (int(n))) 
        delay = delay_range[np.argmax(cross_correlation)]
        print('y2 is ' + str(delay) + 's behind y1')
        self.plot_lag(delay, delay_range, cross_correlation)

    #plot lag 
    def plot_lag(self, delay, delay_range, cross_correlation):
        plt.figure()
        plt.plot(delay_range, cross_correlation)
        plt.title('Lag: ' + str(np.round(delay, 3)) + ' s')
        plt.xlabel('Lag')
        plt.ylabel('Correlation coeff')
        plt.show()

def test_lag_finder(): 
    # Sine sample with some noise and copy to y1 and y2 with a 1-second lag
    sample_rate = 1024 
    y = np.linspace(0, 2*np.pi, sample_rate)
    y = np.tile(np.sin(y), 5)
    y += np.random.normal(0, 5, y.shape)
    y1 = y[int(2.5*sample_rate):int(5.5*sample_rate)]
    y2 = y[int(0*sample_rate):int(3*sample_rate)]

    #plt.plot(y1)
    #plt.plot(y2)
    cc = Cross_correlation()
    cc.lag_finder(y1, y2, sample_rate)

if __name__ == '__main__':
    test_lag_finder()