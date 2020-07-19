let TempTagSet=new Set(),TagSet=new Set();
const showAlert=()=>{
  $("#alert").remove();
  let subwin = $("<div>",{"id":"alert","html":"タイトルと質問内容は入力必須です。"});
  subwin.css({top:"50%",left:"50%",fontSize:"32px",margin:"-4.5em 0em 0em -8em",
  position:"absolute",backgroundColor:"#fff",borderStyle:"groove",borderColor:"#e60033"})
  .appendTo($("body"))
  .animate({opacity:"0"},{duration:"1200",easing:"swing"})
}
const showTagEditor=()=>{
  TagSet.forEach(tag=>TempTagSet.add(tag));
  setTags();
  let subwin=$("#TagEditor");
  subwin.show().css({top:"-30%",left:"50%"})
  .animate({top:$(window).height()/2+$(document).scrollTop()+"px"},500,"swing")
  $("#TagName").on("keydown",(ev)=>{if(ev.keyCode==13)addTag()}).focus();
}
const hideTagEditor=()=>{
  let subwin=$("#TagEditor");
  subwin.animate({top:"-30%"},{duration:500,easing:"swing",complete:()=>subwin.hide()});
  $("#TagName").val('');
  TempTagSet.clear();
}
const addTag=()=>{
  let tag=$("#TagName").val();
  if(!tag)return false;
  if(!TempTagSet.has(tag)){
    TempTagSet.add(tag);
    $("#TagName").val('');
  }
  setTags();
}
const setTags=()=>{
  let html=$("<div>");
  let p;
  TempTagSet.forEach(tag=>{
    p=$("<p></p>",{"class":"Tag","id":tag});
    p.append($("<label>"+tag+"</label>"));
    p.append($("<label></label>",{"class":"removetag","html":"✖"}));
    html.append(p);
  });
  $("#Tags").html(html.html());
}
const submitQuestion=()=>{
  if($("#QuestionTitle").val()==""||$("#QuestionContent").val()==""){
    showAlert();
    return;
  }
  let xhr = new XMLHttpRequest();
  console.log(1);
}
$(document).ready(()=>{
  $("#QuestionSubmit").on("click",()=>{
    let content=$("#QuestionContent").val();
    submitQuestion();
  })
  $("#tagEdit").on("click",()=>{
    showTagEditor();
  })
  $("#TagSubmit").on("click",()=>{
    TagSet.clear();
    TempTagSet.forEach(tag=>TagSet.add(tag));
    hideTagEditor();
  })
  $("#TagCancel").on("click",()=>{
    hideTagEditor();
  })
  $("#Tags").on("click",".removetag",(event)=>{
    event.stopPropagation();
    let parent=event.target.parentNode;
    TempTagSet.delete(parent.id);
    parent.remove();
    $("#TagName").focus();
  })
  $(".home").on("click",()=>{window.location.href="/"})
  $("#main,header").show();
  $("#prev").fadeOut(1000,()=>$("#prev").remove());
})

$(window).on("beforeunload",()=>{
  if($("#QuestionTitle").val()!=""||$("#QuestionContent").val()!=""){
    return "ページ遷移確認";
  }
})
