'''
Created on Apr 14, 2019

@author: Venkat Prasad Krishnamurthy
'''    
    
'''
 This module provides a simple, and incomplete, abstraction to the SenseHAT
 library. It is intended for testing and debugging purposes only.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''
import random 
from sense_hat import SenseHat

class Sense():
    '''
    This class has methods to connect and get sensor values
    from SenseHat
    '''

    def __init__(self):
        self.clearFlag = False
        self.sens = SenseHat()
        print("Sense Hat object successfully created")
    
    def clear(self):
        self.sens.clearFlag = True

    def get_humidity(self):
        return self.sens.get_humidity();
        
    def get_temperature(self):
        return self.sens.get_temperature_from_humidity()
        
    def get_temperature_from_humidity(self):
        return self.sens.get_temperature_from_humidity();
        
    def get_temperature_from_pressure(self):
        return self.sens.get_temperature_from_pressure();
    
    def get_pressure(self):
        return self.sens.get_pressure()
            
    def show_letter(self, val):
        self.sens.show_letter(val)
        
    def get_light_intensity(self):
        lit = 0
        tim = random.randint(0,24)
        if (tim>10 and tim<16):
            lit = random.randint(1075,107527) 
        else:
            lit = random.randint(0,1075)
        
        return lit
    
    def show_message(self, msg):
        self.sens.show_message(str(msg))