from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import webbrowser

class WSUApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=40)
        
        # Create UI elements
        self.label = Label(text='Welcome to Walter Sisulu University Application')
        self.apply_button = Button(text='Apply Now')
        self.status_button = Button(text='Check Application Status')
        
        # Bind button events
        self.apply_button.bind(on_press=self.apply_button_pressed)
        self.status_button.bind(on_press=self.status_button_pressed)
        
        # Add UI elements to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.apply_button)
        layout.add_widget(self.status_button)
        
        return layout
    
    def apply_button_pressed(self, instance):
        # Disable the button while counting
        self.apply_button.disabled = True
        
        # Reset the label text
        self.label.text = '1%'
        
        # Schedule the button counting and message display
        Clock.schedule_interval(self.update_button_text_apply, 0.05)
    
    def status_button_pressed(self, instance):
        # Disable the button while counting
        self.status_button.disabled = True
        
        # Reset the label text
        self.label.text = '1%'
        
        # Schedule the button counting and message display
        Clock.schedule_interval(self.update_button_text_status, 0.05)
    
    def update_button_text_apply(self, dt):
        # Increment the label text and update the button text
        current_percentage = int(self.label.text[:-1])  # Remove '%' sign and convert to integer
        current_percentage += 1
        self.label.text = f'{current_percentage}%'
        
        # Stop the counting when reaching 100%
        if current_percentage >= 100:
            Clock.unschedule(self.update_button_text_apply)
            # Display the welcome message
            self.label.text = 'Welcome to WSU website'
            
            # Open the WSU application link in a web browser
            webbrowser.open('https://wsu.ac.za/index.php/how-to-apply-the-process-wsu')
            
            # Enable the button again
            self.apply_button.disabled = False
    
    def update_button_text_status(self, dt):
        # Increment the label text and update the button text
        current_percentage = int(self.label.text[:-1])  # Remove '%' sign and convert to integer
        current_percentage += 1
        self.label.text = f'{current_percentage}%'
        
        # Stop the counting when reaching 100%
        if current_percentage >= 100:
            Clock.unschedule(self.update_button_text_status)
            # Display the welcome message
            self.label.text = 'Welcome / Wamkelekile'
            
            # Open the WSU application status link in a web browser
            webbrowser.open('https://wsu.ac.za/index.php/student-online-services-portal-wsu')
            
            # Enable the button again
            self.status_button.disabled = False

# Run the WSUApp
if __name__ == '__main__':
    WSUApp().run()
