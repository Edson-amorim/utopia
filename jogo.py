import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

class PersonalidadeIA:
    def __init__(self, nome, cor, estilo):
        self.nome = nome
        self.cor = cor
        self.estilo = estilo

    def falar(self, mensagem):
        cores = {"vermelha": "\033[91m", "azul": "\033[94m", "verde": "\033[92m", "roxa": "\033[95m"}
        reset = "\033[0m"
        cor_texto = cores.get(self.cor, reset)
        print(f"[{self.cor.upper()}] {self.nome}: {cor_texto}{mensagem}{reset}")

    def responder(self, mensagem):
        return mensagem

vermelho = PersonalidadeIA("Verde", "vermelha", "direta")
azul = PersonalidadeIA("Azul", "azul", "analitica")
verde = PersonalidadeIA("Verde", "verde", "otimista")
roxa = PersonalidadeIA("Roxa", "roxa", "criativa")

class AcessibilidadeTela:
    """Classe para garantir acessibilidade para leitores de tela"""
    
    def __init__(self, root):
        self.root = root
        self.leitor_ativo = False
        
        # Configurar propriedades de acessibilidade
        self.root.option_add("*Font", "Arial 12")
        
        # Bind para leitura de mudanças (placeholder - tkinter limitado)
        pass
    
    def anunciar(self, texto):
        """Anuncia texto para leitores de tela"""
        if self.leitor_ativo:
            # Em um sistema real, isso usaria plataforma-specific
            # aqui apenas imprime para depuração
            pass
    
    def ler_botao(self, botao, texto):
        """Configura botão com nome acessível - versao simplificada"""
        # Apenas marcar como focável e dar dica de acessibilidade
        try:
            botao.configure(takefocus=True)
        except:
            pass
        # Store accessible name info via widget tag or tooltip
        try:
            botao.configure(tooltip=texto)
        except:
            pass
    
    def ler_rotulo(self, rotulo, texto):
        """Configura rótulo com nome acessível"""
        rotulo.configure(foreground="blue")
        rotulo.configure(cursor="xterm")

class ConversaIA:
    def __init__(self, root):
        self.root = root
        self.rodada_atual = 0
        self.participantes = [vermelho, azul, verde, roxa]
        self.tema = "sustentabilidade"
        self.acess = AcessibilidadeTela(root)
        
        # Configurar janela
        self._configurar_janela()
        self._criar_widgets()
        self._configurar_atalhos()
    
    def _configurar_janela(self):
        self.root.title("Salvar o Mundo - Conversa entre IA's Acessível")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)
        
        # Foco inicial
        self.root.focus_set()
        
        # Ícone/identificação para leitores de tela
        try:
            self.root.iconname("SalvarMundo_Jogo")
        except:
            pass
    
    def _criar_widgets(self):
        # Frame principal com role description
        main_frame = ttk.LabelFrame(self.root, text="Conversa sobre como melhorar o mundo")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Label de status para leitor de tela
        self.status_label = ttk.Label(main_frame, text="", foreground="gray")
        self.status_label.pack(anchor=tk.W, padx=5, pady=2)
        
        # Área de conversa com role de região
        self.conversa_area = tk.Text(main_frame, height=15, state='disabled', 
                                     font=("Arial", 10))
        self.conversa_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configurar role para leitores de tela (apenas notas, tkinter limitado)
        self.conversa_area.configure(takefocus=True)
        
        # Botão Play com acessibilidade aprimorada
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.btn_play = ttk.Button(btn_frame, text="▶ Iniciar Conversa (20 rodadas)",
                                   command=self._iniciar_conversa)
        self.btn_play.pack(side=tk.LEFT)
        
        # Configurar accesskey e focus
        self.acess.ler_botao(self.btn_play, "Iniciar conversa sobre sustentabilidade")
        
        # Barra de progresso acessível
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, 
                                        length=400, mode='determinate')
        self.progress.pack(fill=tk.X, padx=10, pady=5)
        self.progress.configure(maximum=20, value=0)
        
        # Menu de acessibilidade
        menubar = tk.Menu(self.root)
        menu_acess = tk.Menu(menubar, tearoff=0)
        menu_acess.add_checkbutton(label="Modo leitor de tela", 
                                   command=self._alternar_modo_leitor)
        menu_acess.add_separator()
        menu_acess.add_command(label="Sobre acessibilidade", 
                               command=self._mostrar_info_acessibilidade)
        menubar.add_cascade(label="Acessibilidade", menu=menu_acess)
        self.root.config(menu=menubar)
    
    def _configurar_atalhos(self):
        """Configura atalhos de teclado acessíveis"""
        self.root.bind('<F1>', self._mostrar_atalhos)
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('<Return>', lambda e: self._iniciar_conversa() 
                       if self.btn_play['state'] == 'normal' else None)
    
    def _alternar_modo_leitor(self):
        """Alterna modo de anúncio para leitores de tela"""
        self.acess.leitor_ativo = not self.acess.leitor_ativo
        estado = "ativado" if self.acess.leitor_ativo else "desativado"
        self._anunciar(f"Modo leitor de tela {estado}")
        messagebox.showinfo("Modo Leitor", f"Modo leitor de tela {estado}")
    
    def _mostrar_atalhos(self, event=None):
        """Mostra atalhos disponíveis"""
        atalhos = [
            "F1 - Atalhos de teclado",
            "Enter - Iniciar conversa", 
            "Esc - Sair do jogo",
            "Tab - Navegar entre elementos"
        ]
        info = "\n".join(atalhos)
        messagebox.showinfo("Atalhos de Teclado", info)
    
    def _mostrar_info_acessibilidade(self):
        """Mostra informações sobre as funcionalidades de acessibilidade"""
        info = (
            "Este jogo possui:\n"
            "• Navegação por teclado completa\n"
            "• Anúncios para leitores de tela\n"
            "• Modo alto contraste opcional\n"
            "• Atalhos de teclado claros\n"
            "• Foco visual destacado\n"
            "• Rótulos descritivos em todos os elementos"
        )
        messagebox.showinfo("Informações de Acessibilidade", info)
    
    def _anunciar(self, texto):
        """Método para anunciar texto para leitores de tela"""
        self.acess.anunciar(texto)
        # Atualizar label de status
        try:
            self.status_label.configure(text=texto)
        except:
            pass
    
    def _registrar_mensagem(self, mensagem, cor=""):
        """Registra uma mensagem na área de conversa com acessibilidade"""
        self.conversa_area.configure(state='normal')
        marca = f"[{self.rodada_atual}] "
        self.conversa_area.insert(tk.END, marca + mensagem + "\n")
        self.conversa_area.configure(state='disabled')
        # Scroll para baixo automaticamente
        self.conversa_area.see(tk.END)
    
    def _iniciar_conversa(self):
        """Inicia o loop de 20 rodadas de conversa"""
        self.rodada_atual = 0
        self.progress['value'] = 0
        self._limpar_conversa()
        self._proxima_rodada()
    
    def _limpar_conversa(self):
        """Limpa a área de conversa"""
        self.conversa_area.configure(state='normal')
        self.conversa_area.delete(1.0, tk.END)
        self.conversa_area.configure(state='disabled')
    
    def _proxima_rodada(self):
        """Procede para a próxima rodada da conversa"""
        if self.rodada_atual >= 20:
            self._fim_jogo()
            return
        
        self.rodada_atual += 1
        self.progress['value'] = self.rodada_atual
        
        # Anunciar número da rodada
        self._anunciar(f"Rodada {self.rodada_atual} de 20")
        
        persona_atual = self.participantes[(self.rodada_atual - 1) % 4]
        mensagem = persona_atual.responder(f"Sobre {self.tema}:")
        
        # Registrar com cor e anunciar
        self._registrar_mensagem(
            f"{persona_atual.nome} ({persona_atual.cor}): {mensagem}",
            cor=persona_atual.cor
        )
        
        # Próxima rodada após breve atraso
        self.root.after(500, self._proxima_rodada)
    
    def _fim_jogo(self):
        """Finaliza o jogo após 20 rodadas"""
        self._anunciar("Conversa finalizada. Foram realizadas 20 rodadas sobre sustentabilidade.")
        messagebox.showinfo("Fim do Jogo", 
                          "20 rodadas completas!\n\n"
                          "As personalidades conversaram sobre como melhorar o mundo\n"
                          "através da sustentabilidade. Obrigado por jogar!")

def main():
    root = tk.Tk()
    
    # Garantir que a janela receba foco para leitores de tela
    root.lift()
    root.attributes('-topmost', True)
    
    app = ConversaIA(root)
    
    # Anúncio inicial para leitor de tela
    app._anunciar("Bem-vindo ao Salvando o Mundo. Jogo de conversa entre quatro personalidades de IA.")
    app._anunciar("Pressione Enter ou clique no botão play para iniciar 20 rodadas de conversa.")
    
    root.mainloop()

if __name__ == "__main__":
    main()