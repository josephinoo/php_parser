extends Control
var output=[]

# Declare member variables here. Examples:
# var a: int = 2
# var b: String = "text"


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta: float) -> void:
#	pass


func _on_ToolButton2_pressed() -> void:
	
	var input=$TextEdit.text
	var tmp2 = File.new()
	tmp2.open("tmp2", File.WRITE)
	tmp2.store_string(input)
	tmp2.close()
	#python php_yacc.py test2.txt
	OS.execute("python", ["php_yacc.py", "tmp2"], true, output)
	#print(output[0])
	var tmp=File.new()
	tmp.open("tmp", File.READ)
	var out =tmp.get_as_text()
	if(out==""):
		$"RichTextLabel".text="No hay errores"
	else:
		$"RichTextLabel".text=out
	
	tmp.close()
	tmp.open("tmp", File.WRITE_READ)
	tmp.close()
	
	print(output[0])
	pass # Replace with function body.


func _on_ToolButton_pressed() -> void:
	
	$FileDialog.popup()


func _on_FileDialog_file_selected(path: String) -> void:
	var openFile = File.new()
	openFile.open(path, File.READ)
	$TextEdit.text=openFile.get_as_text()
	openFile.close()


func _on_ToolButton3_pressed() -> void:
	
	var input=$TextEdit.text
	var tmp2 = File.new()
	tmp2.open("tmp2", File.WRITE)
	tmp2.store_string(input)
	tmp2.close()
	#python php_yacc.py test2.txt
	OS.execute("python", ["php_lexico.py", "tmp2"], true, output)
	#print(output[0])
	var tmp=File.new()
	tmp.open("tmp", File.READ)
	var out =tmp.get_as_text()
	if(out==""):
		$"RichTextLabel".text="No hay errores"
	else:
		$"RichTextLabel".text=out
	
	tmp.close()
	tmp.open("tmp", File.WRITE_READ)
	tmp.close()
	
	print(output[0])
	pass # Replace with function body.
