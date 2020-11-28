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
	var tmp = File.new()
	tmp.open("tmp", File.WRITE)
	tmp.store_string(input)
	tmp.close()
	#python php_yacc.py test2.txt
	OS.execute("python3", ["php_yacc.py", "tmp"], true, output)

	$"RichTextLabel".text=output[0]
	pass # Replace with function body.


func _on_ToolButton_pressed() -> void:
	
	$FileDialog.popup()


func _on_FileDialog_file_selected(path: String) -> void:
	var openFile = File.new()
	openFile.open(path, File.READ)
	$TextEdit.text=openFile.get_as_text()
	openFile.close()
