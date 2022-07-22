<template>
  <ion-app>
    <ion-header>
      <ion-row>
        <ion-col size="12">
          <div id="supergrafic"></div>
        </ion-col>
      </ion-row>
      
      <ion-row id="search-box">
        <ion-col id="coluna" size="10">
          <ion-col id="header-search" size="10">
            <ion-col size="12">Local:</ion-col>
            <ion-col size="12">
               <ion-input type="text" ></ion-input>
            </ion-col>
          </ion-col>
        </ion-col>

        <ion-col size="1">
          <div id="lupa"></div>
        </ion-col>

      </ion-row>
    </ion-header>


    <ion-content scroll-y=false id="mainContent">


        <img id="img" src="../../public/assets/icon/map.png"/>
    </ion-content>

    <ion-footer>
        <!-- <ion-row>
            <ion-col id="buttons" size="12">
                <ion-button class="house" expand="full" color="light">
                    <div class="icon-button"></div>
                </ion-button>
                <ion-button class="pin" expand="full" color="light" >
                    <div class="icon-button2"></div>
                </ion-button>
            </ion-col>
      </ion-row> -->
    </ion-footer>
    
  </ion-app>
</template>

<script>

export default  {};
</script>

<style>

@font-face{
  font-family: 'BoschSans-Regular';
  src: url("../../public/fonts/BoschSans-Regular.ttf") ;
}

*{
  padding: 0px;
  margin: 0px;
  font-family: 'BoschSans-Regular';
}

#supergrafic {
  background-image: url("../../public/assets/supergrafic.svg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 10px;
}

#search-box{
  display: flex;
  justify-content: center;
  align-items: center;
  margin:10px 50px;
  background-color: rgb(243, 243, 243);
  border: 1px solid;
  border-top: none;
  border-left: none;
  border-right: none;
}

#header-search{
  display: flex;
  flex-direction: column;
}

#lupa{
  background-image: url("../../public/assets/icon/search.svg");
  background-repeat: no-repeat;
  height: 50px;
   
}





#mainContent{
  background-color: red;
  height: 300px;
}

</style>

