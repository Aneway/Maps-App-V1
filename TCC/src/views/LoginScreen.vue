<template>
  <ion-app>
    <ion-header>
      <ion-grid>
        <ion-row>
          <ion-col>
            <div id="slogan"></div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-header>

    <ion-content scroll-y=false id="mainContent">

      <ion-row>
        <img id="sloganMap" src="../../public/assets/icon/map.png"/>
        <ion-label class="labelTitle">Welcome</ion-label>

        <ion-item>
          <ion-label class="labelInput" position="floating">EDV</ion-label>
          <ion-input class="input"></ion-input>
        </ion-item>

        <ion-item>
          <ion-label class="labelInput" position="floating">Password</ion-label>
          <ion-input class="input" type="password"></ion-input>
        </ion-item>

        <ion-button>Enter</ion-button>
        <router-link to="/verify">First Acess</router-link>
      </ion-row>

    </ion-content>

    <ion-footer>
      <ion-grid>
        <ion-row>
          <ion-col>
            <div id="supergraphic"></div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-footer>
    
  </ion-app>
</template>

<script lang="ts">
import { IonApp, IonInput, IonCol,IonRow,IonGrid, IonHeader, IonLabel, IonItem, IonButton} from '@ionic/vue';
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import { archiveOutline, archiveSharp, bookmarkOutline, bookmarkSharp, heartOutline, heartSharp, mailOutline, mailSharp, paperPlaneOutline, paperPlaneSharp, trashOutline, trashSharp, warningOutline, warningSharp } from 'ionicons/icons';

export default defineComponent({
  name: 'App',
  components: {
    IonApp, 
    IonInput,
    IonCol,
    IonRow,
    IonGrid,
    IonHeader,
    IonLabel,
    IonItem,
    IonButton
  },
  setup() {
    const selectedIndex = ref(0);
    const appPages = [
      {
        title: 'Inbox',
        url: '/folder/Inbox',
        iosIcon: mailOutline,
        mdIcon: mailSharp
      },
      {
        title: 'Outbox',
        url: '/folder/Outbox',
        iosIcon: paperPlaneOutline,
        mdIcon: paperPlaneSharp
      },
      {
        title: 'Favorites',
        url: '/folder/Favorites',
        iosIcon: heartOutline,
        mdIcon: heartSharp
      },
      {
        title: 'Archived',
        url: '/folder/Archived',
        iosIcon: archiveOutline,
        mdIcon: archiveSharp
      },
      {
        title: 'Trash',
        url: '/folder/Trash',
        iosIcon: trashOutline,
        mdIcon: trashSharp
      },
      {
        title: 'Spam',
        url: '/folder/Spam',
        iosIcon: warningOutline,
        mdIcon: warningSharp
      }
    ];
    const labels = ['Family', 'Friends', 'Notes', 'Work', 'Travel', 'Reminders'];
    
    const path = window.location.pathname.split('folder/')[1];
    if (path !== undefined) {
      selectedIndex.value = appPages.findIndex(page => page.title.toLowerCase() === path.toLowerCase());
    }
    
    const route = useRoute();
    
    return { 
      selectedIndex,
      appPages, 
      labels,
      archiveOutline, 
      archiveSharp, 
      bookmarkOutline, 
      bookmarkSharp, 
      heartOutline, 
      heartSharp, 
      mailOutline, 
      mailSharp, 
      paperPlaneOutline, 
      paperPlaneSharp, 
      trashOutline, 
      trashSharp, 
      warningOutline, 
      warningSharp,
      isSelected: (url: string) => url === route.path ? 'selected' : ''
    }
  }
});
</script>

<style lang="scss" scoped>

@font-face{
  font-family: 'BoschSans-Regular';
  src: url("../../public/fonts/BoschSans-Regular.ttf") ;
}

*{
  padding: 0px;
  margin: 0px;
  font-family: 'BoschSans-Regular';
}

#supergraphic{
  background-image: url("../../public/assets/supergrafic.svg");
  background-size: cover;
  height: 10px;
  background-repeat: no-repeat;
}

#slogan{
  background-image: url("../../public/assets/logotype.svg");
  background-size: contain; 
  height: 70px;
  background-repeat: no-repeat;
}

#mainContent{
  height: 100vh;
  *{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  #sloganMap{
  height: 150px;
  }
  .labelTitle{
  color: #002742;
  font-family: 'BoschSans-Regular';
  font-size: 36px; 
  font-weight: bold;
  margin-bottom: 10px;
  }
  ion-row{
    margin-top: 40px;
  }
  .labelInput{
    align-items: left;
    justify-content: left;
    // margin-left: -55px;
  }
  .input{
    height: 100px;
  }
  ion-button{
    --border-radius: none;
    --background: #0a6f9d;
    --background-activated: #003253;
    width: 115px;
    height: 45px;
    margin-top: 30px;
    margin-bottom: 10px;
  }
}

</style>
