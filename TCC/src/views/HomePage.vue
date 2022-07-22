<template>
  <ion-app>
    <ion-header>
      <ion-row>
      <ion-col size="12">
        <div id="supergrafic"></div>
      </ion-col>
    </ion-row>
    <ion-row>
      <ion-col size="12">
        <div id="logotype"></div>
      </ion-col>
    </ion-row>
    </ion-header>
    <ion-content scrollY="true" id="main-content">
      <ion-row class="menuRow">
        <ion-col class="menuItem" size-md="7" size="5">
          <router-link class="menuLink" to="map">
              <img src="../../public/assets/icon/map.svg">
              <h3>Map</h3>
          </router-link>
        </ion-col>
        <ion-col class="menuItem" size-md="7" size="5">
          <router-link class="menuLink" to="restaurant">
              <img src="../../public/assets/icon/cutlery.svg">
              <h3>Restaurant</h3>
          </router-link>
        </ion-col>
      </ion-row>
      <ion-row class="menuRow">
        <ion-col class="menuItem" size-md="7" size="5">
          <router-link class="menuLink" to="information">
              <img src="../../public/assets/icon/info-i.svg">
              <h3>Information</h3>
          </router-link>
        </ion-col>
      </ion-row>
    </ion-content>
  </ion-app>
</template>

<script lang="ts">
export default {
  
  data(){
      return{
        supergrafic: require('../../public/assets/supergrafic.svg')
      }
  }
}
</script>

<style lang="scss">
*{
  padding: 0px;
  margin: 0px;
}

#main-content{
  height: 85vh;
  overflow: auto;
}

#supergrafic{
  width: 100%;
  height: 10px;
  background-image: url('../../public/assets/supergrafic.svg');
  background-repeat: no-repeat;
  background-size: cover;
}
#logotype{
  height: 50px;
  background-image: url('../../public/assets/logotype.svg');
  background-repeat: no-repeat;
  background-size: contain;
  border-bottom: 1px solid #E0E2E5;
}

.menuRow{
  width: 100%;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  .menuItem{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
    background-color: #007BC0;
    a.menuLink{
      color: white;
    }  
    .menuLink{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      width: 100%;
      padding: 10px;
      h3{
        margin: 0px;
        color: white;
      }
      img{
        width: 50%;
      }
    }
  }
}
</style>