import customtkinter
#from PIL import image

#main_window_definition

customtkinter.set_appearance_mode("dark")

class FrameLeft(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky='nswe')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(master=self, text='ClickBot',
                                        font=('Roboto Medium', -16),
                                        fg_color='teal')
        self.title_label.grid(row=0, column=0, columnspan=1, padx=20, sticky='n')

        self.button_tctl_menu = customtkinter.CTkButton(master=self, text="Switch to Tactical Menu", command=UserInterface.button_tctl_menu)
        self.button_tctl_menu.grid(row=1, column=0, columnspan=1, padx=0, pady=10, sticky='n')

        self.button_tctl_menu_config = customtkinter.CTkButton(master=self, text="Tactical Menu config.", command=UserInterface.button_tctl_menu_config)
        self.button_tctl_menu_config.grid(row=2, column=0, columnspan=1, padx=0, pady=0, sticky='n')

class Tabview(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(padx=0, pady=0)
        self._segmented_button.configure(height=50)
        self.add(' '*50 +'ClickBot'+' '*50)
        self.add(' '*50+'AimAssist Clickbot'+' '*50)
        self.add(' '*50+'Whatsapp Scraperbot'+' '*50)
        self.add(' '*50+'Instagram Scraperbot'+' '*50)
        self.add(' '*50+'Custom Scraperbot'+' '*50)
        self.FirstTab(self.tab(' '*50 +'ClickBot'+' '*50))
    
    def FirstTab(self, tab):
        #'ClickBot' Tabview Tab SetUp 
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)
        #Clickbot 'Container' Frame
        first_tab_frame = customtkinter.CTkFrame(master=tab, fg_color="red")
        first_tab_frame.grid(row=0, column=0, sticky='nwe')

        first_tab_frame.grid_columnconfigure(0, weight=1)
        first_tab_frame.grid_columnconfigure(1, weight=1)
        first_tab_frame.grid_columnconfigure(2, weight=1)
        first_tab_frame.grid_columnconfigure(3, weight=1)


        first_tab_frame.grid_rowconfigure(0, weight=1)
        first_tab_frame.grid_rowconfigure(1, weight=1)
        
        #First title label
        click_bot_label = customtkinter.CTkLabel(master= first_tab_frame, text='Begin: Clicking / KeySpan',
                                                       font=('Roboto Medium', -26), pady=10, padx =5)
        click_bot_label.grid(row=0, column=0, columnspan= 2, sticky='nsw')
        #Clicking interval
        click_bot_interval_label = customtkinter.CTkLabel(master= first_tab_frame, text='Interval:',
                                                       font=('Roboto Medium', -10))
        click_bot_interval_label.grid(row=1, column=0, sticky='nswe')
        click_bot_interval_entry = customtkinter.CTkEntry(master= first_tab_frame, placeholder_text='1', width=40, height=40)
        click_bot_interval_entry.grid(row=1, column=1, pady=5, sticky='nswe')

        #Starting delay
        click_bot_starting_delay_label = customtkinter.CTkLabel(master= first_tab_frame, text='Starting delay:',
                                                       font=('Roboto Medium', -10) )
        click_bot_starting_delay_label.grid(row=1, column=2, sticky='nswe')
        click_bot_starting_delay_entry = customtkinter.CTkEntry(master= first_tab_frame, placeholder_text='1', width=40, height=40)
        click_bot_starting_delay_entry.grid(row=1, column=3, pady=5, sticky='nswe')

        #KeySpan Selector
        click_bot_keyspan_label = customtkinter.CTkLabel(master = first_tab_frame, text='KeySpan:',
                                                         font=('Roboto Medium', -10))
        click_bot_keyspan_label.grid(row=2, column=0, sticky='nswe')
        click_bot_keyspan_checkbox = customtkinter.CTkCheckBox(master = first_tab_frame, text=' ')
        click_bot_keyspan_checkbox.grid(row=2, column= 1, pady=5, sticky='w')

        #Key Selector
        click_bot_key_label = customtkinter.CTkLabel(master = first_tab_frame, text='Key:',
                                                         font=('Roboto Medium', -10))
        click_bot_key_label.grid(row=2, column=2, sticky='nswe')
        click_bot_key_label = customtkinter.CTkEntry(master= first_tab_frame, placeholder_text='k', width=40, height=40)
        click_bot_key_label.grid(row=2, column=3, pady=5, sticky='nswe')

        #Mouse btn Selector
        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)
        click_bot_mouse_button_label = customtkinter.CTkLabel(master = first_tab_frame, text='Mouse key:',
                                                         font=('Roboto Medium', -10))
        click_bot_mouse_button_label.grid(row=3, column=0, pady=5, sticky='nswe')

        optionmenu_var = customtkinter.StringVar(value="Left")
        click_bot_mouse_button_optMenu = customtkinter.CTkOptionMenu(master = first_tab_frame, values=["Left", "Right"],
                                                        command=optionmenu_callback,
                                                        variable=optionmenu_var)
        click_bot_mouse_button_optMenu.grid(row=3, column=1, pady=5, sticky='w')

        #Begin Clicking
        def button_event():
            print("button pressed")

        click_bot_start_button = customtkinter.CTkButton(master = first_tab_frame, text="Begin ClickBot", command=button_event)
        click_bot_start_button.grid(row=4, column=3, pady=10, padx=5, sticky='e')

        #Second title label
        click_bot_label_2 = customtkinter.CTkLabel(master= first_tab_frame, text='WorkFlow:',
                                                       font=('Roboto Medium', -26), pady=10, padx=5)
        click_bot_label_2.grid(row=5, column=0, columnspan= 2, sticky='nsw')







#Right frame that holds tabview
class FrameRight(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=1, sticky='nswe', padx=20, pady=20)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)
        #Tabview SetUp
        self.tabview = Tabview(master=self, fg_color='blue')
        self.tabview.grid(row=0, column=0, sticky='n')
        self.tabview.grid_rowconfigure(0, weight=1)
        self.tabview.grid_columnconfigure(0, weight=1)
    

class UserInterface(customtkinter.CTk): #App
    WIDTH = 1400
    HEIGHT = 750
    MINWIDTH = 800
    MINHEIGHT = 500

    def __init__(self):
        super().__init__()
        #self.iconbitmap(default=)
        self.title('ClickBot')
        self.geometry(f'{UserInterface.WIDTH}x{UserInterface.HEIGHT}')
        self.minsize(UserInterface.MINWIDTH, UserInterface.MINHEIGHT)
        # call .on_closing() custom function when app gets closed
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        #----Base Grid:----
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #Frame_left SetUp:
        self.frame_left = FrameLeft(self)

        #Frame_right SetUp: Frame right contains the right tab
        self.frame_right = FrameRight(self)


    def button_tctl_menu():
        print("button pressed")
    
    def button_tctl_menu_config():
        print("button pressed")

    def button_tctl_menu_config():
        print("button pressed")

    # close the app when the window is closed
    def on_closing(self, event=0) -> None:
        self.destroy()





'''
tabview = ctk.CTkTabview(main_window)
tabview.pack(padx=20, pady=20)

tabview.add('WhatsApp')  # add tab at the end
tabview.add('Twitter')  # add tab at the end
tabview.set('WhatsApp')  # set currently visible tab
tabview.tab('WhatsApp').grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(master=tabview.tab('WhatsApp'))
button.place(x=10, y=10)


def tactical_menu():
    main_window.iconify()
    t_m_window = ctk.CTkToplevel(main_window, fg_color="teal") #garantees new window on top in case of system delay
    t_m_window.geometry("100x200")

btn_tactical_menu = ctk.CTkButton(master=main_window,text="Switch to Tactical Menu",command=tactical_menu)
'''
if __name__ == '__main__':
    Ui = UserInterface()
    Ui.mainloop()




