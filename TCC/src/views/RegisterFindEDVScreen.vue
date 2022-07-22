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

    <ion-content id="main-content">
      <ion-grid fixed>
        <ion-row>
          <ion-col size="12">
            <img id="sloganMap" src="../../public/assets/icon/search.svg" />
          </ion-col>
          <ion-col size="12">
            <ion-label class="labelTitle">Verify your EDV</ion-label>
          </ion-col>
          <ion-col size="12">
            <ion-item>
              <ion-input v-model="edv" type="number"></ion-input>
            </ion-item>
          </ion-col>
          <ion-col size="12">
            <ion-button @click="SearchEDV"> Search </ion-button>
          </ion-col>
          <ion-col size="12">
            <router-link to="/">The login already exist?</router-link>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-app>
</template>

<script>
import {userData} from '../store/userInformations'
import axios from "axios";
import {
  IonApp,
  IonGrid,
  IonRow,
  IonCol,
  IonHeader,
  IonLabel,
  IonInput,
  IonButton,
  alertController,
} from "@ionic/vue";
export default {
  name: "RegisterFindEDVScreen",
  components: {
    IonApp,
    IonGrid,
    IonRow,
    IonCol,
    IonHeader,
    IonLabel,
    IonInput,
    IonButton,
  },
  data() {
    return {
      edv: null,
    };
  },
  methods: {
    SearchEDV() {
      axios
        .post("http://127.0.0.1:5000/", {
          EDV: this.edv,
        })
        .then((e) => {
          this.ConfirmUser(e.data);
        })
        .catch(() => {
          this.EDVNotFound();
        });
    },
    async EDVNotFound() {
      const alert = await alertController.create({
        header: "EDV Not Found",
        subHeader: "Verify whether you type correctly and try again",
        buttons: ["Ok"],
      });

      await alert.present();
    },
    async ConfirmUser(data) {
      const alert = await alertController.create({
        header: "That's you?",
        subHeader:
          "This EDV is relationated with " + data.Nome + " this are you?",
        buttons: [
          "No",
          {
            text: "Yes",
            role: "yes",
            handler: () => {
              const information = userData()
              information.inputData(data.EDV,data.Nome,data.Email,data.Telefone)
              this.$router.push("/register");
            },
          },
        ],
      });

      await alert.present();
    },
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: "BoschSans-Regular";
  src: url("../../public/fonts/BoschSans-Regular.ttf");
}

#slogan {
  background-image: url("../../public/assets/logotype.svg");
  background-size: contain;
  height: 50px;
  background-repeat: no-repeat;
}

#main-content {
  display: flex;
  justify-content: center;
  align-items: center;
  ion-grid {
    *{
    margin-top: 5px;
    }
    height: 100%;
    width: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
    ion-row {
      display: flex;
      justify-content: center;
      align-items: center;
      ion-col {
        display: flex;
        justify-content: center;
        align-items: center;
        ion-input {
          padding: 10px;
          display: flex;
          justify-content: center;
          align-items: center;
          text-align: center;
          font-size: 20px;
        }
      }
    }
  }
}
#sloganMap {
  height: 150px;
}
.labelTitle {
  color: #002742;
  font-family: "BoschSans-Regular";
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}
</style>