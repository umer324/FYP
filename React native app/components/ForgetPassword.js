import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Alert,
  TextInput,
  TouchableOpacity,
} from "react-native";

const ForgetPassword = ({ navigation, route }) => {
  const [email, setEmail] = React.useState("");

  const otpBtnClick = () => {
    Alert.alert(userEmail);
    if (email === "") {
      Alert.alert(
        "Send OTP",
        "Please enter the Email",
        [{ text: "OK", onPress: () => console.log("OK Pressed") }],
        { cancelable: false }
      );
    } else {
      navigation.navigate("Home");
    }
  };
  const { item } = route.params;
  const { name } = item;

  return (
    <View style={styles.container}>
      <Text style={styles.logo}>Forget Password</Text>
      <View style={styles.inputView}>
        <TextInput
          style={styles.inputText}
          placeholder="Email..."
          placeholderTextColor="#003f5c"
          onChangeText={(text) => {
            setEmail(text);
          }}
        />
      </View>
      <TouchableOpacity
        onPress={() => {
          navigation.navigate("Login");
        }}
      >
        <Text style={styles.forgot}>Remember Password ? Sign In</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.loginBtn} onPress={otpBtnClick}>
        <Text style={styles.loginText}>Send OTP</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#003f5c",
    alignItems: "center",
    justifyContent: "center",
  },
  logo: {
    fontWeight: "bold",
    fontSize: 50,
    color: "#fb5b5a",
    marginBottom: 40,
    marginLeft: 40,
  },
  inputView: {
    width: "80%",
    backgroundColor: "#465881",
    borderRadius: 25,
    height: 50,
    marginBottom: 20,
    justifyContent: "center",
    padding: 20,
  },
  inputText: {
    height: 50,
    color: "white",
  },
  forgot: {
    color: "white",
    fontSize: 11,
  },
  loginBtn: {
    width: "80%",
    backgroundColor: "#fb5b5a",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    marginBottom: 10,
  },
  loginText: {
    color: "white",
  },
});

export default ForgetPassword;
