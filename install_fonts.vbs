Set objShell = CreateObject("Shell.Application")
Set objFolder = objShell.Namespace("C:\Program Files (x86)\PC Manager\fonts")

For Each strFile In objFolder.Items
    If LCase(Right(strFile.Path, 4)) = ".ttf" Then
        objShell.Namespace("C:\Windows\Fonts").CopyHere strFile.Path
    End If
Next

Set objShell = Nothing
Set objFolder = Nothing
