<script language="javascript">
	document.getElementById("submitButton").onclick = function(){
		if(document.getElementById("id_recall_statement").value.length < 150)
		{
			alert("输入文本长度不能小于150个字符!");
			return false;
		}
		return true;
	}
</script>