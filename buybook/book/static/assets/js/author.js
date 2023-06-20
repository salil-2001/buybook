
    
function AgeCalculate(){
    
    var birth_date = new Date($('.birth_date').val());
    var death_date =  new Date($(".death_date").val());
    var birth_year=parseInt(birth_date.getFullYear())
    var death_year = parseInt(death_date.getFullYear())
    var age=death_year - birth_year
    $("#age").val(age)
    
    


}

