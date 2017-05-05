/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableHighlight
} from 'react-native';

export default class MyButton extends Component {
  _onPressButton() {
   // console.log("You tapped the button!");
	get
  }

  render() {
    let expl = 'gooodooodood';
    return (
      <View>
      	  <TextInput
		placeholder={'input your phone'}
	  />
        <TouchableHighlight  onPress={this._onPressButton}>
	  <Text style={styles.btnText}>查号</Text>
        </TouchableHighlight>
	<Text>{expl}</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  phoneInput: {
   color: 'blue',
   fontWeight: 'bold',
   fontSize: 30,
  },
  btnText: {
    color: 'red',
	justifyContent: 'center',

  }
});

AppRegistry.registerComponent('MyButton', () => MyButton);
