#passamos um argumento para o print
#argumento é o conteudo dentro do print
#\r \n -> CRLF
#\n ->LF (quebra linha)
#Print != print (Prirnt com letra maiuscula não existe no python apenas com letra minuscula)
print(12, 34, 1011, sep='-', end='\r\n')
print(56, 78, sep='_', end='\n')
print(9, 10, 15, 60, sep='--', end='##\n')

#argumentos não nomeados  varios argumentos para exibir
#argumentos nomeados 

''''
     ----importante:----
*Argumentos não nomeados (Positional Arguments): Passados na ordem definida.
*Argumentos nomeados (Keyword Arguments): Passados usando o nome do parâmetro.
*Mistura de argumentos: Os não nomeados vêm antes dos nomeados.
*Argumentos com valores padrão: Usados se nenhum valor for fornecido.
*Argumentos variáveis: *args para não nomeados e **kwargs para nomeados.
*Ordem dos parâmetros: Posicionais, valores padrão, *args, nomeados, **kwargs.'''