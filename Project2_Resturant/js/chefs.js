(function(){
    let ChefDetailData = document.querySelectorAll(".chef-detail .data")
    let cards = document.querySelectorAll('.all-chefs .row .chef')
    cards.forEach((card)=>{
        card.addEventListener('click' , ()=>{
            ChangChefDetail(card.attributes)
        })
    })
    function ChangChefDetail(card){
        for(let i =0 ; i<ChefDetailData.length ; i++){
            console.log(ChefDetailData[i])
            console.log(card[i])
            // console.log(card[card.length-1].value)

            if(ChefDetailData[i].hasAttribute('data-width')){
                ChefDetailData[i].setAttribute('data-width',card[i].value)
                console.log(true)
            }
            else{
                ChefDetailData[i].textContent = card[i].value
            }
        }
    }
})()
