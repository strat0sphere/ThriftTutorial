
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;


public class MultiplicationClient {

 public static void main(String[] args) {

  try {
   TTransport transport;

   transport = new TSocket("localhost", 9090);
   transport.open();

   TProtocol protocol = new TBinaryProtocol(transport);
   MultiplicationService.Client client = new MultiplicationService.Client(protocol);

   System.out.println(client.multiply(100, 200));

   transport.close();
  } catch (TTransportException e) {
   e.printStackTrace();
  } catch (TException x) {
   x.printStackTrace();
  }
 }

}