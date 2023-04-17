# Gerador-de-Senha

Este é um código Python que gera senhas aleatórias com base nas preferências do usuário.

A senha pode ter letras maiúsculas e minúsculas, números e símbolos.

Este é um código Python que gera senhas aleatórias baseadas nas preferências do usuário.
O usuário escolhe o comprimento da senha e quantas letras e números deseja incluir. O código usa os módulos `random` e `string` para gerar caracteres aleatórios e obter os caracteres válidos, respectivamente.

O programa garante que a senha tenha pelo menos seis caracteres e permite que o usuário ajuste a senha gerada.

Se o usuário especificar que deseja mais caracteres do que letras e números combinados, o código preenche os caracteres restantes com símbolos aleatórios.

Após a geração da senha, o código mistura aleatoriamente os caracteres na lista passwordl e exibe a senha resultante para o usuário. O usuário é solicitado a verificar se a senha gerada atende às suas necessidades e pode ajustar a senha, se necessário.

Esse código pode ser útil para pessoas que precisam criar senhas fortes e aleatórias para suas contas online, já que o código permite que o usuário personalize a senha de acordo com suas preferências.

Exemplo de uso:

 Digamos que você queira uma senha de 12 caracteres, com 8 letras e 4 números.

Você pode executar o código e fornecer as seguintes entradas:

```cmd
How long do you want your password to be? 12
How many letters do you want (they will be in uppercase and lowercase) 8
And how many numbers do you want? 4
```
O código gerará uma senha aleatória que atenda às suas especificações e exibirá a senha na tela, como:

```cmd
Y6nR1sU7&kWj
Does this password satisfies you??
[Y] yes
[N] no
```

Se a senha atender às suas necessidades, você pode usar essa senha para criar sua conta. Caso contrário, você pode executar o código novamente e ajustar suas preferências até que esteja satisfeito com a senha gerada.

Lembre-se de que é importante escolher senhas fortes e aleatórias para proteger suas informações pessoais online. Esse código pode ser útil para criar senhas fortes e aleatórias com base em suas preferências pessoais.
## Contribuição


Se você deseja contribuir para este projeto, siga os seguintes passos:

1. Faça um fork do repositório
2. Crie um branch com sua contribuição: `git checkout -b minha-contribuicao`
3. Realize as mudanças e faça o commit: `git commit -m 'Minha contribuição'`
4. Faça o push para o seu branch: `git push origin minha-contribuicao`
5. Crie um Pull Request no repositório original

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
