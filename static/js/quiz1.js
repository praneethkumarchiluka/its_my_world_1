 var score = 0; //Set score to 0
var total = 15; //Total number of questions
var point = 1; //Points per correct answer
var highest = total * point;
var n1=0
//Initializer
function init(){
	//set correct answers
	sessionStorage.setItem('a1','d');
	sessionStorage.setItem('a2','b');
	sessionStorage.setItem('a3','b');
	sessionStorage.setItem('a4','b');
	sessionStorage.setItem('a5','d');
	sessionStorage.setItem('a6','b');
	sessionStorage.setItem('a7','c');
	sessionStorage.setItem('a8','a');
	sessionStorage.setItem('a9','b');
	sessionStorage.setItem('a10','b');
	sessionStorage.setItem('a11','c');
	sessionStorage.setItem('a12','b');
	sessionStorage.setItem('a13','a');
	sessionStorage.setItem('a14','d');
	sessionStorage.setItem('a15','c');
}

$(document).ready(function(){
	//Hide all questions
	$('.questionForm').hide();
	
	//Show first question
	$('#q1').show();
	
	$('.questionForm #submit').click(function(){
		//Get data attributes
		current = $(this).parents('form:first').data('question');
		next = $(this).parents('form:first').data('question')+1;
		//Hide all questions
		$('.questionForm').hide();
		//Show next question
		$('#q'+next+'').fadeIn(300);
		process(''+current+'');
		return false;
	});
});

//Process the answers
function process(n){
	//Get input value
	var submitted = $('input[name=q'+n+']:checked').val();
	if(submitted == sessionStorage.getItem('a'+n+'')){
			score = score + point;
	}else {
	n1++
	}
		
	if(n == total){	
		$('#results').html('<h3>Your final score is: '+score+' out of '+highest+' worng answered '+n1+'</h3>');
		if(score == highest){
			$('#results').append('<p>You are an Python master!');
		} else if(score == highest - point || score == highest - point - point){
			$('#results').append('<p>Good Job!');
		}
	}
	return false;
}

//Add event listener
window.addEventListener('load',init,false);