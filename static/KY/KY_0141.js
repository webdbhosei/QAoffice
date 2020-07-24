let TempTagSet=new Set(),TagSet=new Set(),posted=false;
const showAlert=(message="注意")=>{
  $("#alert").remove();
  let subwin = $("<div>",{"id":"alert","html":message});
  subwin.css({top:"50%",left:"50%",fontSize:"32px",margin:"-4.5em 0em 0em -8em",
  position:"absolute",backgroundColor:"#fff",borderStyle:"groove",borderColor:"#e60033"})
  .appendTo($("body"))
  .animate({opacity:"0"},{duration:"2000",easing:"swing",complete:()=>subwin.hide()})
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

const getCookie=(name)=> {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const submitQuestion=(event)=>{
  event.stopPropagation();
  console.log(0);
  if(!$("#QuestionSubject").val()||!$("#QuestionContent").val()){
    showAlert("タイトルと質問内容は入力必須です。");
    return false;
  }
  let data={'SUBJECT':$("#QuestionSubject").val(),'CONTENT':$("#QuestionContent").val(),'TAGS':JSON.stringify(TagSet)};
  // let xhr = new XMLHttpRequest();
  // xhr.open("POST","post/question");
  // xhr.setRequestHeader("X-CSRFToken",getCookie("csrftoken"));
  // xhr.send(data);
  posted = true;
  console.log(data);
  return true;
}

$(document).ready(()=>{
  $("#QuestionContentWrapper").children().attr({'id':"QuestionContent",'placeholder':"質問内容を入力してください。"});
  $("#QuestionSubjectWrapper input").attr({'id':"QuestionSubject",'placeholder':'科目'});
  $("#QuestionForm").on("submit",submitQuestion)
  $("#tagEdit").on("click",()=>{
    showTagEditor();
  })
  $("#TagSubmit").on("click",()=>{
    TagSet.clear();
    TempTagSet.forEach(tag=>TagSet.add(tag));
    $("#QuestionTags").val(JSON.stringify(TagSet));
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
  if(!posted&&($("#QuestionSubject").val()||$("#QuestionContent").val())){
    return "ページ遷移確認";
  }
})
