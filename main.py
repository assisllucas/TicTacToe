import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.1.0')  # Versão do Kivy

class TicTacToeApp(App):

    def build(self):
        self.title = 'Jogo da Velha'
        self.player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.layout = GridLayout(cols=3)

        for i in range(3):
            for j in range(3):
                button = Button(font_size=40)
                button.bind(on_release=self.button_pressed)
                self.layout.add_widget(button)

        return self.layout

    def button_pressed(self, instance):
        row, col = self.get_button_position(instance)

        if self.board[row][col] == '':
            self.board[row][col] = self.player
            instance.text = self.player

            if self.check_winner():
                self.show_popup(f'Jogador {self.player} venceu!')
                self.reset_game()
            elif self.check_draw():
                self.show_popup('Empate!')
                self.reset_game()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def get_button_position(self, instance):
        index = self.layout.children.index(instance)
        row = index // 3
        col = index % 3
        return row, col

    def check_winner(self):
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for button in self.layout.children:
            button.text = ''
        self.player = 'X'

    def show_popup(self, message):
        box = BoxLayout(orientation='vertical')
        label = Label(text=message, font_size=30)
        close_button = Button(text='Fechar', size_hint=(1, 0.2))
        box.add_widget(label)
        box.add_widget(close_button)

        popup = Popup(title='Fim de Jogo', content=box, size_hint=(0.5, 0.5))
        close_button.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    TicTacToeApp().run()
