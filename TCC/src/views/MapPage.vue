<template>
  <ion-app id="main-content">
    <ion-header>
      <ion-row>
        <ion-col size="12">
          <div id="barrinha"></div>
        </ion-col>
      </ion-row>
      <ion-row id="header-box">
        <ion-col id="coluna" size="10">
          <ion-col id="header-search" size="10">
            <ion-col size="12">
              Local:
            </ion-col>
            <ion-col size="12">
              <ion-input type="text" ></ion-input>
            </ion-col>
          </ion-col>
          
        </ion-col>
        <ion-col size="1">
            <div id="lupa">

            </div>
        </ion-col>
      </ion-row>

      <!-- MAPA -->

      <ion-row>
        <ion-col id="map" size="12"></ion-col>
      </ion-row>
      <!-- MAPA -->
<!-- //////////////////////////////////////////////////// -->
      <!-- BOTÕES -->
      <ion-row>
        <ion-col id="buttons" size="12">
          <ion-button class="house" expand="full" color="light">
            <div class="icon-button"></div>
          </ion-button>
          <ion-button class="pin" expand="full" color="light" >
            <div class="icon-button2"></div>
          </ion-button>
        </ion-col>
      </ion-row>
      <!-- BOTÕES -->
    </ion-header>
  </ion-app>
</template>

<script>

export default  {};
</script>

<style>
* {
  padding: 0px;
  margin: 0px;
}
#header-search{
  display: flex;
  flex-direction: column;
}
#main-content {
  height: 100vh;
}
#barrinha {
  background-image: url("../../public/assets/supergrafic.svg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 10px;
}
#lupa{
  background-image: url("../../public/assets/icon/search.svg");
  background-repeat: no-repeat;
  height: 50px;
   
}
#col-prin{
  margin-top: 4%;
  margin-left: 3%;


}
#header-box{
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
#map{
  background-color: rgb(4, 158, 219);
  height: 80vh;
}
#buttons{
  background-color: white;
  height: 20vh;
  justify-content: center;
  display: flex;
}

.icon-button{
  background-image: url("../../public/assets/icon/home.svg");
  padding: 20px;
}
.icon-button2{
  background-image: url("../../public/assets/icon/locator.svg");
  padding: 20px;

}
.house{
  border: 1px solid;
  border-color: rgb(4, 158, 219);
  border-top: none;
  border-bottom: none;
  border-left: none;
    --box-shadow:none;
}

.pin{
  --box-shadow:none;
}

</style>

