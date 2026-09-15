import wx

class JanelaPrincipal(wx.Frame):
    def __init__(self, *args, **kw):
        super(JanelaPrincipal, self).__init__(*args, **kw)
        
        
        self.SetTitle("Exemplo de Botão e Campo de Frase")
        self.SetSize(300, 200)
        
       
        painel = wx.Panel(self)
        
        
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        
      
        self.txt_frase = wx.TextCtrl(painel, value="Digite sua frase aqui", style=wx.TE_PROCESS_ENTER)
        sizer_principal.Add(self.txt_frase, 0, wx.ALL | wx.EXPAND, 10)
        
        
        botao_acao = wx.Button(painel, label="Exibir Frase")
        sizer_principal.Add(botao_acao, 0, wx.ALL | wx.CENTER, 10)
        
        
        self.lbl_resultado = wx.StaticText(painel, label="")
        sizer_principal.Add(self.lbl_resultado, 0, wx.ALL | wx.CENTER, 10)
        
        
        botao_acao.Bind(wx.EVT_BUTTON, self.ao_clicar_botao)
        
        
        painel.SetSizer(sizer_principal)
        self.Centre()

    def ao_clicar_botao(self, event):
       
        frase_digitada = self.txt_frase.GetValue()
        
        
        self.lbl_resultado.SetLabel(f"Você digitou: {frase_digitada}")

if __name__ == '__main__':
    app = wx.App()
    janela = JanelaPrincipal(None)
    janela.Show()
    app.MainLoop()
