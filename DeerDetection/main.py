import queue
import numpy as np


from gui_video_output import Gui_video_output
from processThread import ProcessThread


class Main:
    def __init__(self, title, url):
        # Send the URL through the pipeline 
        self.gui = Gui_video_output()
        
        
        #intialize variable to hold current webcam video frame
        self.current_frame = None
        
        #create a queue to fetch and execute callbacks passed 
        #from background thread
        self.callback_queue = queue.LifoQueue(maxsize = 1) # OR QUEUE
        
        #create a thread to fetch webcam feed video
        self.process_thread = ProcessThread(self.gui, self.callback_queue, url)
           
        #register callback for being called when GUI window is closed
        self.gui.root.protocol("WM_DELETE_WINDOW", self.on_gui_closing)
        
        self.fps = 33
        

        #start video source
        self.start_video()
        
        #start fetching video
        self.fetch_source_video()
    
    def on_gui_closing(self):
        self.process_thread.stop()
        self.process_thread.join()
        self.process_thread.release_resources()
        
        self.gui.root.destroy()

    def start_video(self):
        self.process_thread.start()
        
    def fetch_source_video(self):
            try:
                self.fetch_source_video
                #while True:
                #try to get a callback put by the process thread
                #if there is no callback and call_queue is empty
                #then this function will throw a Queue.Empty exception 
                callback = self.callback_queue.get_nowait()
                callback()
                #self.app_gui.root.update_idletasks()
                
                    
            except queue.Empty:
                self.gui.root.after(self.fps, self.fetch_source_video)

            else:
                self.gui.root.after(self.fps, self.fetch_source_video)


           

    
    
    def launch(self):
        self.gui.launch()
        
    def __del__(self):
        self.process_thread.stop()


# ## The Launcher Code For GUI

# In[10]:

if __name__ == "__main__":
        url = "https://www.youtube.com/watch?v=8SDm48ieYP8"

main = Main("Title", url)
main.launch()